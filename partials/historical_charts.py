from partials.chart_filter import chart_filter

historical_charts = f"""
	<div class="row row-cols-1 justify-content-center mx-1">

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title">Validator Queue (ETH)</h5>
		    <div class="card-text">
		    	<div class="text-center text-sm-end">
			    	{chart_filter("queueChart")}
				</div>
		    	<div>
					<canvas id="queueChart"></canvas>
				</div>
			</div>
		  </div>
		</div>

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title">Queue Wait Time (days)</h5>
		    <div class="card-text">
		    	<div class="text-center text-sm-end">
			    	{chart_filter("waitChart")}
				</div>
		    	<div>
					<canvas id="waitChart"></canvas>
				</div>
			</div>
		  </div>
		</div>

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title">Active Validators</h5>
		    <div class="card-text">
		    	<div class="text-center text-sm-end">
			    	{chart_filter("validatorChart")}
				</div>
		    	<div>
					<canvas id="validatorChart"></canvas>
				</div>
			</div>
		  </div>
		</div>

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title">Supply Staked</h5>
		    <div class="card-text">
		    	<div class="text-center text-sm-end">
			    	{chart_filter("stakedChart")}
				</div>
		    	<div>
					<canvas id="stakedChart"></canvas>
				</div>
			</div>
		  </div>
		</div>

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title">Staking APR (7d)</h5>
		    <div class="card-text">
		    	<div class="text-center text-sm-end">
			    	{chart_filter("aprChart")}
				</div>
		    	<div>
					<canvas id="aprChart"></canvas>
				</div>
			</div>
		  </div>
		</div>

	</div>
"""
