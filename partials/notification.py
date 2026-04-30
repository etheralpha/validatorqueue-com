enable_notification = "true" # "true" or "false"
notification_id = 1 # must increment when creating a new message
notification_msg = '<a href="https://ethstaker.org/forms/staking-landscape-survey-2026" target="_blank">Take the 2026 Staking Landscape Survey!</a>' # Best when under 100 characters
notification_expiration = 1779555600 # epoch time in seconds


notification_css = r"""
  <style type="text/css">
    #notification {
      position: fixed;
      z-index: 101;
      bottom: 0;
      left: 0;
      right: 0;
      color: var(--bs-dark);
      text-align: center;
      overflow: hidden;
      box-shadow: 0 -0.5rem 1rem rgba(0,0,0,.15);
      background-color: var(--bs-body-bg);
    }
    #notification a {
      color: var(--bs-dark);
    }
    #notificationClose {
      cursor: pointer;
    }
  </style>
  """

notification_js = f"""
  <script type="text/javascript">
    window.onload = showNotification();
    // Loads/shows notification bar if users hasn't closed it yet
    function showNotification() {{
      const notificationName = "notification-{notification_id}";
      const hideNotification = localStorage.getItem(notificationName);
      const timestamp = Math.round(Date.now()/10000)*10;
      if (hideNotification != "true" && timestamp < {notification_expiration}) {{
        const notification = document.getElementById("notification");
        notification.classList.remove("d-none");
      }}
    }}
    // Hides notification bar when user closes it
    function hideNotification() {{
      let notification = document.getElementById("notification");
      notification.classList.add("d-none");
      const notificationName = "notification-{notification_id}";
      localStorage.setItem(notificationName, "true");
    }}
  </script>
  """

notification_html = f"""
  {notification_css}
  <!-- notification -->
  <div id="notification" class="d-none d-flex bg-warning">
    <span id="notification_msg" class="flex-grow-1 py-2 ps-3 pe-1">
      {notification_msg}
    </span>
    <span id="notificationClose" class="mx-2 my-auto py-1 px-2" onclick="hideNotification()">✕</span>
  </div>
  {notification_js}
  """

def notification():
  if enable_notification:
    return notification_html
