rule auto_rule_20250726211940_8980 {
  strings:
    $o0 = "x1868" wide ascii nocase
    $o1 = "xFFFFECEC" wide ascii nocase
    $o2 = "x7AB9" wide ascii nocase
    $o3 = "x399B00006E10LL" wide ascii nocase
    $o4 = "x2439u" wide ascii nocase
  condition:
    4 of ($o*)
}