from fastapi import APIRouter, Depends, Request, Response, HTTPException, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User
from app.core.security import verify_password, create_access_token

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )

@router.post("/login")
async def login(request: Request, email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.email})
    redirect = RedirectResponse(url="/", status_code=302)
    redirect.set_cookie(key="access_token", value=f"Bearer {token}", httponly=True)
    return redirect


@router.get("/logout")
async def logout(request: Request):
    redirect = RedirectResponse(url="/login", status_code=302)
    redirect.delete_cookie(key="access_token")
    return redirect