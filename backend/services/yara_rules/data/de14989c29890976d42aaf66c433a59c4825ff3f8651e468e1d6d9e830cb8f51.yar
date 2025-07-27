rule auto_rule_20250727023835_2425 {
  strings:
    $o0 = "cef_force_web_plugin_shutdown" wide ascii nocase
    $o1 = "acos" wide ascii nocase
    $o2 = "dbl_10127398" wide ascii nocase
    $o3 = "cef_v8value_create_function" wide ascii nocase
  condition:
    4 of ($o*)
}