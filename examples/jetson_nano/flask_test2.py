from flask import Flask, request, redirect, url_for, render_template, json, render_template_string, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def control_panel():
    print('request.form:', request.form)
    
    if request.method == 'POST':
        if request.form.get('button') == 'button-play':
            print("play button pressed")

        elif request.form.get('button') == 'button-exit':
            print("exit button pressed")

        elif request.form.get('slide'):
            volume = request.form.get('slide')
            print('volume:', volume)
            #return jsonify({'volume': volume})
            return json.dumps({'volume': volume})

    print('render')
    return render_template_string('''<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

    <title>Slider</title>
  </head>
  <body>
    <div class="container" id="control_panel_1">
  <form action="/" method ="post" enctype="multipart/form-data" id="form">
    <div class="row">
            <div class="col">
              <button class="btn btn-primary" button type="submit" name="button" value="button-play">PLAY</button>

              <button class="btn btn-primary" button type="submit" name="button" value="button-exit">EXIT</button>

              <input id="slide" type="range" min="1" max="100" step="1" value="10" name="slide">
              <div id="sliderAmount"></div>
            </div>
    </div>
  </form>

    <!--- SCRIPTS --->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
<script>
  var slide = document.getElementById('slide'),
    sliderDiv = document.getElementById("sliderAmount");

slide.onchange = function() {
    sliderDiv.innerHTML = this.value;
    $.post({
            url: '/',
            data: $('form').serialize(),
            success: function(response){
                alert(response);
                alert(response.volume);             // works with jsonify()
                alert(JSON.parse(response).volume); // works with json.dumps()
                console.log(response);
            },
            error: function(error){
                alert(response);
                console.log(error);
            }
        });
}
</script>
</html>''')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
