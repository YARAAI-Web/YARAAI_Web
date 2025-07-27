rule auto_rule_20250727031446_3458 {
  strings:
    $o0 = "lpAppName" wide ascii nocase
    $o1 = "presbits" wide ascii nocase
    $o2 = "hsz1" wide ascii nocase
  condition:
    3 of ($o*)
}