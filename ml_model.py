import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

MODEL_FILE = "model.pkl"

# 🔹 Expanded training data for better accuracy
train_data = [
    # Documents
    ("resume.pdf", "Documents"), ("report.docx", "Documents"), ("notes.txt", "Documents"),
    ("budget.xlsx", "Documents"), ("presentation.pptx", "Documents"), ("data.csv", "Documents"),
    ("readme.md", "Documents"), ("assignment.pdf", "Documents"), ("invoice.docx", "Documents"),

    # Music
    ("song.mp3", "Music"), ("music.wav", "Music"), ("track01.flac", "Music"),
    ("audio.m4a", "Music"), ("beat.aac", "Music"), ("recording.mp3", "Music"),

    # Images
    ("photo.jpg", "Images"), ("image.png", "Images"), ("wallpaper.jpeg", "Images"),
    ("icon.png", "Images"), ("picture.gif", "Images"), ("logo.svg", "Images"),
    ("profile.webp", "Images"), ("screenshot.bmp", "Images"),

    # Code
    ("program.py", "Code"), ("code.cpp", "Code"), ("script.js", "Code"),
    ("index.html", "Code"), ("styles.css", "Code"), ("main.java", "Code"),
    ("header.h", "Code"), ("backend.php", "Code"), ("build.sh", "Code"),

    # Shortcuts
    ("chrome.lnk", "Shortcuts"), ("vscode.lnk", "Shortcuts"), ("browser.lnk", "Shortcuts"),
    ("game_shortcut.url", "Shortcuts"), ("desktop.lnk", "Shortcuts"),

    # Executables
    ("setup.exe", "Executables"), ("installer.msi", "Executables"), ("app.exe", "Executables"),
    ("patch.bat", "Executables"), ("update.exe", "Executables"), ("tool.msi", "Executables")
]

# Separate filenames and labels
train_files, train_labels = zip(*train_data)

# 🔹 Training Process
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(train_files)

model = MultinomialNB()
model.fit(X, train_labels)

# 🔹 Save the updated model
with open(MODEL_FILE, "wb") as f:
    pickle.dump((model, vectorizer), f)

def predict_folder(filename):
    with open(MODEL_FILE, "rb") as f:
        model, vectorizer = pickle.load(f)

    X_test = vectorizer.transform([filename])
    prediction = model.predict(X_test)[0]

    return prediction

if __name__ == "__main__":
    print("Model retrained with expanded data successfully!")