from flask import Flask, render_template, url_for, flash, redirect
from form_books_rent import RentCalcForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'

@app.route("/rent",defaults={'total': None}, methods=['GET', 'POST'])
@app.route("/rent/<float:total>", methods=['GET', 'POST'])
def rent(total):
    form_org = RentCalcForm()
    if form_org.validate_on_submit():
        total_regular = 0
        if form_org.regular_rent_duration.data > 2:
            total_regular = form_org.regular_books_count.data
            total_regular = total_regular+form_org.regular_books_count.data*(form_org.regular_rent_duration.data-2)*1.5
        else:
            total_regular = form_org.regular_books_count.data*form_org.regular_rent_duration.data
        if total_regular == 1:
            total_regular = 2

        total_fiction = form_org.fiction_books_count.data*form_org.fiction_rent_duration.data*3
        if form_org.novel_rent_duration.data < 3 and form_org.novel_books_count.data > 0 :
            total_novel = 4.5
        else:
            total_novel = form_org.novel_books_count.data*form_org.novel_rent_duration.data*1.5



        total = total_regular + total_fiction + total_novel

        return redirect(url_for('rent', total=total))
    return render_template('login.html', form=form_org, total=total)


if __name__ == '__main__':
    app.run(debug=True)
