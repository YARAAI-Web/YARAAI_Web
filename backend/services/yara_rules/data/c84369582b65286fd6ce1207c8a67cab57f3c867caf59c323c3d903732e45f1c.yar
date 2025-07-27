rule auto_rule_20250726213302_5437 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "dword_418020" wide ascii nocase
    $o2 = "__isctype_mt" wide ascii nocase
    $o3 = "_NLG_Notify1" wide ascii nocase
  condition:
    4 of ($o*)
}