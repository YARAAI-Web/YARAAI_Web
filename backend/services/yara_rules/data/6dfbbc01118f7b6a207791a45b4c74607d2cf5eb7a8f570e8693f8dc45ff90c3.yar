rule auto_rule_20250726091653_8692 {
  strings:
    $o0 = "xB8077220" wide ascii nocase
    $o1 = "xB8078B1C" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}