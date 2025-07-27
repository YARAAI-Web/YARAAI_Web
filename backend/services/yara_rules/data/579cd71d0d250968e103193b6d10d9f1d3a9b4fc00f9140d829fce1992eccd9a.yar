rule auto_rule_20250726164407_6816 {
  strings:
    $o0 = "dbgrpt" wide ascii nocase
    $o1 = "_CrtIsValidPointer" wide ascii nocase
  condition:
    all of them
}