rule auto_rule_20250726172740_9931 {
  strings:
    $o0 = "GetDlgCtrlID" wide ascii nocase
    $o1 = "SuspendThread" wide ascii nocase
    $o2 = "cchBufferLength" wide ascii nocase
    $o3 = "lpIconName" wide ascii nocase
  condition:
    4 of ($o*)
}