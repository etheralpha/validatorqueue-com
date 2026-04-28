from partials.chart_filter import chart_filter

historical_charts = f"""
	<div id="historicalCharts" class="row row-cols-1 justify-content-center mx-1">

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title" id="validator-queue-eth">Validator Queue (ETH) <a href="#validator-queue-eth" class="anchor-link">#</a></h5>
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
		    <h5 class="card-title" id="queue-wait-time">Queue Wait Time (days) <a href="#queue-wait-time" class="anchor-link">#</a></h5>
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
		    <h5 class="card-title" id="active-validators">Active Validators <a href="#active-validators" class="anchor-link">#</a></h5>
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
		    <h5 class="card-title" id="credentials-pct">Credentials (%) <a href="#credentials-pct" class="anchor-link">#</a></h5>
		    <div class="card-text">
		    	<div class="text-center text-sm-end">
			    	{chart_filter("credentialsPercentChart")}
				</div>
		    	<div>
					<canvas id="credentialsPercentChart"></canvas>
				</div>
			</div>
		  </div>
		</div>

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title" id="credentials-delta">Credentials (Δ) <a href="#credentials-delta" class="anchor-link">#</a></h5>
		    <div class="card-text">
		    	<div class="text-center text-sm-end">
			    	{chart_filter("credentialsDiffChart")}
				</div>
		    	<div>
					<canvas id="credentialsDiffChart"></canvas>
				</div>
			</div>
		  </div>
		</div>

		<div class="card shadow border-light mt-4">
		  <div class="card-body">
		    <h5 class="card-title" id="supply-staked">Supply Staked <a href="#supply-staked" class="anchor-link">#</a></h5>
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
		    <h5 class="card-title" id="staking-apr">Staking APR (7d) <a href="#staking-apr" class="anchor-link">#</a></h5>
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
