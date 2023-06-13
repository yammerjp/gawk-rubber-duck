# 🐥gawk rubber duck🐥

This application is a service that provides a buddy for gawk programmers, the rubber duck. The rubber duck will answer questions about gawk that you enter in the input field.

This application uses OpenAI API and Llama-Index to generate answers, and the <a href="https://www.gnu.org/software/gawk/manual/" target="_blank">gawk user manual</a> is used as the input document for Llama-Index. Therefore, the content of the sections of the manual that appear with the responses is governed by the original license.

## Usage

```shell
$ docker run -p 8080:8080 --env OPENAI_API_KEY=${OPENAI_API_KEY} --env FLASK_LIMITER_STORAGE_URI="memory://" "ghcr.io/yammerjp/gawk-rubber-duck"
```

## Libraries Used

- LlamaIndex
- Flask
- Flask-Limiter
