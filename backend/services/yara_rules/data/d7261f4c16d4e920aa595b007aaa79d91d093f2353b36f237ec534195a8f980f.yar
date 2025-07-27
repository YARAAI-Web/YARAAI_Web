rule auto_rule_20250726140202_9669 {
  strings:
    $o0 = "dword_469B7C" wide ascii nocase
    $o1 = "_inc" wide ascii nocase
    $o2 = "CPtoLCID" wide ascii nocase
  condition:
    3 of ($o*)
}