name=input("Enter your file with extensions: ").lower().strip().split(".")[-1]

match name:
    case "gif":
       print("image/"+"gif")
    case "jpg" | "jpeg":
       print("image/"+"jpeg")
    case "png":
       print("image/"+"png")
    case "pdf":
       print("application/pdf")
    case "txt":
       print("text/plain")
    case "zip":
       print("application/zip")
    case "bin":
       print("application/octet-stream")
    case _:
      print("application/octet-stream")
    