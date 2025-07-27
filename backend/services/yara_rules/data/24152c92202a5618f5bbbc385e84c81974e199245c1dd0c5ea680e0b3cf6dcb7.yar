rule auto_rule_20250726085458_5304 {
  strings:
    $o0 = "__acrt_uninitialize_critical" wide ascii nocase
  condition:
    all of them
}