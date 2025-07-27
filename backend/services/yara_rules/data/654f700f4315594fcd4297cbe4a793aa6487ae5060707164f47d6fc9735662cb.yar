rule auto_rule_20250726114007_2249 {
  strings:
    $o0 = "cef_remove_web_plugin_path" wide ascii nocase
  condition:
    all of them
}