rule auto_rule_20250726211105_5228 {
  strings:
    $o0 = "_onexit_lk" wide ascii nocase
    $o1 = "CPtoLCID" wide ascii nocase
    $o2 = "dword_45CF0C" wide ascii nocase
    $o3 = "UnwindUp0_0" wide ascii nocase
    $o4 = "byte_45D040" wide ascii nocase
  condition:
    4 of ($o*)
}