# columns: [...questions]
# responses: { 'question': [...responses], 'outcome': [...outcomes] }
# response: { 'question': [response] }

from flask import Flask, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	data = request.json
	
	pima = pd.DataFrame(data.responses)
	
	x = pima[data.columns]
	y = pima.outcome

	clf = DecisionTreeClassifier(criterion='entropy', max_depth=3).fit(x, y)
	y_pred = clf.predict(pd.DataFrame(data.response))

	return y_pred[0]


if __name__ == '__main__':
	app.run(threaded=True, port=5000)
