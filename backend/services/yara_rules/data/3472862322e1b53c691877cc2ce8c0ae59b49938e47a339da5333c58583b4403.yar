rule auto_rule_20250726073716_9240 {
  strings:
    $o0 = "asc_10040E08" wide ascii nocase
    $o1 = "probe" wide ascii nocase
  condition:
    all of them
}