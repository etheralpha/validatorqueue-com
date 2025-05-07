def churn_schedule(active):
	return ""
#   return f"""
# 	<div class="accordion mx-1 mt-2" id="accordionChurnSchedule">
# 		<div class="accordion-item">
# 			<h2 class="accordion-header">
# 				<button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">Churn Schedule</button>
# 			</h2>
# 			<div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionChurnSchedule">
# 				<div class="accordion-body">
# 					<table class="table">
# 						<tr>
# 							<td>Active Validators</td>
# 							<td>Churn Per Epoch</td>
# 							<td>Churn Per Day</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 0 and active < 327680 else ""}>
# 							<td>0</td>
# 							<td>4</td>
# 							<td>900</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 327680 and active < 393216 else ""}>
# 							<td>327,680</td>
# 							<td>5</td>
# 							<td>1,125</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 393216 and active < 458752 else ""}>
# 							<td>393,216</td>
# 							<td>6</td>
# 							<td>1,350</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 458752 and active < 524288 else ""}>
# 							<td>458,752</td>
# 							<td>7</td>
# 							<td>1,575</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 524288 and active < 589824 else ""}>
# 							<td>524,288</td>
# 							<td>8</td>
# 							<td>1,800</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 589824 and active < 655360 else ""}>
# 							<td>589,824</td>
# 							<td>9</td>
# 							<td>2,025</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 655360 and active < 720896 else ""}>
# 							<td>655,360</td>
# 							<td>10</td>
# 							<td>2,250</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 720896 and active < 786432 else ""}>
# 							<td>720,896</td>
# 							<td>11</td>
# 							<td>2,475</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 786432 and active < 851968 else ""}>
# 							<td>786,432</td>
# 							<td>12</td>
# 							<td>2,700</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 851968 and active < 917504 else ""}>
# 							<td>851,968</td>
# 							<td>13</td>
# 							<td>2,925</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 917504 and active < 983040 else ""}>
# 							<td>917,504</td>
# 							<td>14</td>
# 							<td>3,150</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 983040 and active < 1048576 else ""}>
# 							<td>983,040</td>
# 							<td>15</td>
# 							<td>3,375</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1048576 and active < 1114112 else ""}>
# 							<td>1,048,576</td>
# 							<td>16</td>
# 							<td>3,600</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1114112 and active < 1179648 else ""}>
# 							<td>1,114,112</td>
# 							<td>17</td>
# 							<td>3,825</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1179648 and active < 1245184 else ""}>
# 							<td>1,179,648</td>
# 							<td>18</td>
# 							<td>4,050</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1245184 and active < 1310720 else ""}>
# 							<td>1,245,184</td>
# 							<td>19</td>
# 							<td>4,275</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1310720 and active < 1376256 else ""}>
# 							<td>1,310,720</td>
# 							<td>20</td>
# 							<td>4,500</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1376256 and active < 1441792 else ""}>
# 							<td>1,376,256</td>
# 							<td>21</td>
# 							<td>4,725</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1441792 and active < 1507328 else ""}>
# 							<td>1,441,792</td>
# 							<td>22</td>
# 							<td>4,950</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1507328 and active < 1572864 else ""}>
# 							<td>1,507,328</td>
# 							<td>23</td>
# 							<td>5,175</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1572864 and active < 1638400 else ""}>
# 							<td>1,572,864</td>
# 							<td>24</td>
# 							<td>5,400</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1638400 and active < 1703936 else ""}>
# 							<td>1,638,400</td>
# 							<td>25</td>
# 							<td>5,625</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1703936 and active < 1769472 else ""}>
# 							<td>1,703,936</td>
# 							<td>26</td>
# 							<td>5,850</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1769472 and active < 1835008 else ""}>
# 							<td>1,769,472</td>
# 							<td>27</td>
# 							<td>6,075</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1835008 and active < 1900544 else ""}>
# 							<td>1,835,008</td>
# 							<td>28</td>
# 							<td>6,300</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1900544 and active < 1966080 else ""}>
# 							<td>1,900,544</td>
# 							<td>29</td>
# 							<td>6,525</td>
# 						</tr>
# 						<tr{' class="active"' if active >= 1966080 else ""}>
# 							<td>1,966,080</td>
# 							<td>30</td>
# 							<td>6,750</td>
# 						</tr>
# 					</table>
# 				</div>
# 			</div>
# 		</div>
# 	</div>
# """
