rule auto_rule_20250726152154_7758 {
  strings:
    $o0 = "fill_with_EOS_dwords" wide ascii nocase
    $o1 = "GetStringTypeW" wide ascii nocase
    $o2 = "dword_45F2AC" wide ascii nocase
    $o3 = "dword_45F634" wide ascii nocase
    $o4 = "_seh_longjmp_unwind" wide ascii nocase
  condition:
    4 of ($o*)
}