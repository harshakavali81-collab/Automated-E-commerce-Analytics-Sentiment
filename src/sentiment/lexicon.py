"""Inspectable, negation-aware baseline; NOT validated model accuracy."""
import re
POS={"amazing","excellent","good","great","love","comfortable","reliable","fast","useful","perfect","nice"}
NEG={"bad","terrible","poor","broken","slow","disappointing","difficult","awful","unreliable"}
NOT={"not","never","no"}
def score(text):
    words=re.findall(r"[a-z]+",text.lower());total=0
    for i,w in enumerate(words):
        v=1 if w in POS else -1 if w in NEG else 0
        if v and any(x in NOT for x in words[max(0,i-2):i]):v=-v
        total+=v
    return total
def label(text):
    v=score(text)
    return "positive" if v>0 else "negative" if v<0 else "neutral"
