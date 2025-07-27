rule auto_rule_20250726072148_9132 {
  strings:
    $o0 = "aSoftware" wide ascii nocase
    $o1 = "lpszReturnBuffer" wide ascii nocase
  condition:
    all of them
}