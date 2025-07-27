rule auto_rule_20250726173350_8747 {
  strings:
    $o0 = "_itoa" wide ascii nocase
    $o1 = "SignalObjectAndWait" wide ascii nocase
  condition:
    all of them
}