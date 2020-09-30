web: gunicorn \
             --bind  "0.0.0.0:${PORT}" \
             --access-logfile '-' \
             --error-logfile '-' \
             --workers 1 \
             --worker-class gthread \
             --threads 20 \
             --timeout 60 \
             --limit-request-line 0 \
             --limit-request-field_size 0 \
             "${FLASK_APP}"