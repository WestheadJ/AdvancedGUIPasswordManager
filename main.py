import base64,os,random,sqlite3,string,bcrypt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

