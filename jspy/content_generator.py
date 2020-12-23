from yattag import Doc

doc, tag, text, line = Doc(
    defaults={
        'title': 'reveal.js',
        'contact_message': 'You just won the lottery!'
    },
    errors={
        'contact_message': 'Your message looks like spam.'
    }
).ttl()
stag = doc.stag

with tag('div', klass="reveal"):
    with tag('label'):
        line('h1', 'Welcome')
        with tag('form'):
            stag('input')

content = document.getElementById('content')
content.innerHTML = doc.getvalue()
