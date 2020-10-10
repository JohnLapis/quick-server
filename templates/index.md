# Poemas pegos de algum site

{% for poem in poems %}

## {{ poem.title }}

{% for verse in poem.text %}

{{ verse }}

{% endfor %}

---

{% endfor %}
