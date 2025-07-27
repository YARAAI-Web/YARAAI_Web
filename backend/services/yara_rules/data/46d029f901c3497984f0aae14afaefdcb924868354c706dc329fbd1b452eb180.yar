rule auto_rule_20250726084244_7749 {
  strings:
    $o0 = "dwLevel" wide ascii nocase
    $o1 = "dwDesiredAccess" wide ascii nocase
    $o2 = "DdeAccessData" wide ascii nocase
  condition:
    3 of ($o*)
}