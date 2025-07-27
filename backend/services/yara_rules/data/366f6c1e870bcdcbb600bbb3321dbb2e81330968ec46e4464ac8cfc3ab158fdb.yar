rule auto_rule_20250726092158_9121 {
  strings:
    $o0 = "ActiveWindow" wide ascii nocase
    $o1 = "_SEH_epilog" wide ascii nocase
    $o2 = "off_476D28" wide ascii nocase
    $o3 = "dword_4766D0" wide ascii nocase
  condition:
    4 of ($o*)
}