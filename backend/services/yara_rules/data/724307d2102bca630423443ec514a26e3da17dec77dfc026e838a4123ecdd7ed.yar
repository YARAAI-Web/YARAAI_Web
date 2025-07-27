rule auto_rule_20250726143930_3361 {
  strings:
    $o0 = "ZwCreateFile" wide ascii nocase
    $o1 = "dword_7830C" wide ascii nocase
    $o2 = "MaximumLength" wide ascii nocase
  condition:
    3 of ($o*)
}