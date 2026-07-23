import requests

mobiles = [
    {"name": "Nokia", "color": "Black", "price": 1000},
    {"name": "Samsung", "color": "Blue", "price": 25000},
    {"name": "Realme", "color": "Yellow", "price": 18000},
    {"name": "OnePlus", "color": "Green", "price": 35000},
    {"name": "Vivo", "color": "White", "price": 22000},
    {"name": "Oppo", "color": "Purple", "price": 21000},
    {"name": "Redmi", "color": "Silver", "price": 16000},
    {"name": "iPhone", "color": "Gold", "price": 85000},
    {"name": "Motorola", "color": "Gray", "price": 19000},
    {"name": "Google Pixel", "color": "Pink", "price": 65000}
]

for mobile in mobiles:
    res = requests.post(
        "http://localhost:3000/mobiles",
        json=mobile
    )
    print(res.status_code)
    print(res.json())


laptops = [{
    "brand": "HP",
    "model": "Pavilion",
    "price": 62000
},{
      "brand": "Dell",
      "model": "Inspiron 15",
      "price": 55000
    },{
      "brand": "Lenovo",
      "model": "IdeaPad Slim 5",
      "price": 64000
    },
    {
      "brand": "Acer",
      "model": "Aspire 7",
      "price": 68000
    },
    {
      "brand": "ASUS",
      "model": "Vivobook 15",
      "price": 62000
    },
    {
      "brand": "Apple",
      "model": "MacBook Air M3",
      "price": 134900
    },
    {
      "brand": "MSI",
      "model": "GF63 Thin",
      "price": 92000
    },
    {
      "brand": "Samsung",
      "model": "Galaxy Book4",
      "price": 78000
    },
    {
      "brand": "LG",
      "model": "Gram 16",
      "price": 125000
    },
    {
      "brand": "Huawei",
      "model": "MateBook D16",
      "price": 98000
    }
  ]

for laptop in laptops:
 res = requests.post(
    "http://localhost:3000/laptops",
    json=laptop
)

 print(res.status_code)
 print(res.json())

books= [{ "title": "Python Basics", "author": "John Smith", "price": 450 },
{ "title": "Java Programming", "author": "James Lee", "price": 550 },
    { "title": "SQL Essentials", "author": "David Brown", "price": 400 },
    { "title": "C Programming", "author": "Dennis Ritchie", "price": 350 },
    { "title": "Web Development", "author": "Alice Green", "price": 600 },
    { "title": "Data Structures", "author": "Mark Wilson", "price": 700 },
    { "title": "Machine Learning", "author": "Andrew Ng", "price": 900 },
    { "title": "AI Fundamentals", "author": "Tom White", "price": 850 },
    { "title": "Cloud Computing", "author": "Sarah Miller", "price": 750 },
    { "title": "Cyber Security", "author": "Kevin Mitnick", "price": 800 }
  ]
for book in books:
   res = requests.post("http://localhost:3000/laptops",json=book)
   print(res.status_code)
   print(res.json())

movies= [
    { "title": "Inception", "genre": "Sci-Fi", "rating": 8.8 },
    { "title": "Interstellar", "genre": "Sci-Fi", "rating": 8.7 },
    { "title": "The Dark Knight", "genre": "Action", "rating": 9.0 },
    { "title": "Avengers: Endgame", "genre": "Action", "rating": 8.4 },
    { "title": "Titanic", "genre": "Romance", "rating": 7.9 },
    { "title": "Joker", "genre": "Drama", "rating": 8.4 },
    { "title": "3 Idiots", "genre": "Comedy", "rating": 8.4 },
    { "title": "Baahubali", "genre": "Action", "rating": 8.0 },
    { "title": "RRR", "genre": "Action", "rating": 7.8 },
    { "title": "Pushpa", "genre": "Action", "rating": 7.6 }
  ]
for movie in movies:
   res=requests.post("http://localhost:3000/laptops",json=movie)
   print(res.status_code)
   print(res.json())

songs= [
    { "title": "Shape of You", "artist": "Ed Sheeran", "duration": "3:53" },
    { "title": "Blinding Lights", "artist": "The Weeknd", "duration": "3:20" },
    { "title": "Perfect", "artist": "Ed Sheeran", "duration": "4:23" },
    { "title": "Believer", "artist": "Imagine Dragons", "duration": "3:24" },
    { "title": "Levitating", "artist": "Dua Lipa", "duration": "3:23" },
    { "title": "Naatu Naatu", "artist": "Rahul Sipligunj", "duration": "3:34" },
    { "title": "Srivalli", "artist": "Sid Sriram", "duration": "3:44" },
    { "title": "Kesariya", "artist": "Arijit Singh", "duration": "4:28" },
    { "title": "Butta Bomma", "artist": "Armaan Malik", "duration": "3:15" },
    { "title": "Samajavaragamana", "artist": "Sid Sriram", "duration": "3:49" }
  ]
for song in songs:
   res = requests.post("http://localhost:3000/laptops",json=song)
   print(res.status_code)
   print(res.json())