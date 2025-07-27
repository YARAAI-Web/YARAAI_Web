rule auto_rule_20250726235850_9999 {
  strings:
    $o0 = "dword_418350" wide ascii nocase
    $o1 = "lpWindowName" wide ascii nocase
  condition:
    all of them
}