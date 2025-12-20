class ArabicDetection:
    def __init__(self, *args, **kwargs):
        super(ArabicDetection, self).__init__(*args, **kwargs)

    def categorize_by_characters(self, word: str) -> str:
        arabic_chars = set("حصضطظع")

        persian_chars = set("پچژگ")

        if any(c in word for c in arabic_chars):
            return "arabic"
        elif any(c in word for c in persian_chars):
            return "persian"
        else:
            return "unknown"
