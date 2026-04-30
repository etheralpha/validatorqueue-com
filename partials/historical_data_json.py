import json

def historical_data_json(historical_data, historical_conversion_data):
  return f"""
    <script type="text/javascript">
      const historical_data = {json.dumps(historical_data)};
      const historical_conversion_data = {json.dumps(historical_conversion_data)};
    </script>
  """
