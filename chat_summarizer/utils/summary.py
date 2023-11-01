from transformers import PegasusForConditionalGeneration, PegasusTokenizer


class Summarizer:
    def __init__(self) -> None:
        print("summarizer initialized")
        self.tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-multi_news")
        print("tokenizer downloaded")
        self.model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-multi_news")
        print("model downloaded")

    def generate_abstractive_summary(self, text: str) -> str:
        tokens = self.tokenizer(text, max_length=128, truncation=True, padding="longest", return_tensors="pt")
        summary = self.model.generate(**tokens)
        return self.tokenizer.decode(summary[0])
