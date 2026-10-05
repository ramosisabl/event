from flask import Flask, render_template, request, redirect, uri_for

app = Flask(__name__)

eventos = [
    {"id": 1, "nome": "Show de rock", "ingressos_disponiveis": 10};