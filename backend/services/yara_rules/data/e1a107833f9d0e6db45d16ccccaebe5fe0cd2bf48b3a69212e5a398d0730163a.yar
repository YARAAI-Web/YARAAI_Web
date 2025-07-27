rule auto_rule_20250726130702_5339 {
  strings:
    $o0 = "uFormat" wide ascii nocase
    $o1 = "idAttachTo" wide ascii nocase
    $o2 = "GetDCEx" wide ascii nocase
    $o3 = "dword_41A708" wide ascii nocase
    $o4 = "hmenu" wide ascii nocase
  condition:
    5 of ($o*)
}