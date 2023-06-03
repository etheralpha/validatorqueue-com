import json

def footer(historical_data):
	return f"""
		<hr class="mt-5">

	    <p class="text-center my-0 text-muted">
	    	Made by <a href="https://etheralpha.org" target="_blank">Ether Alpha</a> with <small>❤️</small>
		</p>

		<p class="text-center my-4">
			<a href="https://github.com/etheralpha/validatorqueue-com" target="_blank">
				<svg height="40" width="40" aria-hidden="true" viewBox="0 0 16 16" version="1.1" data-view-component="true" class="github-link"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
			</a>
		</p>

		<script type="text/javascript">
			const historical_data = {json.dumps(historical_data)}
		</script>
		<script src="assets/js/main.js" type="application/javascript"></script>
		<script src="https://cdn.jsdelivr.net/npm/chart.js@4.3.0/dist/chart.umd.min.js"></script>
		<script src="https://cdn.jsdelivr.net/npm/moment@2.29.4/moment.min.js"></script>
		<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-moment@^1"></script>
		<script src="assets/js/historicalCharts.js" type="application/javascript"></script>
	"""
