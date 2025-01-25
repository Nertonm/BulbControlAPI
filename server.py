import uvicorn

if __name__ == '__main__':
    uvicorn.run("services.lampada_service:app", port=8080, reload=True)