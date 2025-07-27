rule auto_rule_20250726192235_7654 {
  strings:
    $o0 = "dword_42A028" wide ascii nocase
    $o1 = "off_45C90C" wide ascii nocase
    $o2 = "dword_45D264" wide ascii nocase
    $o3 = "ualAllocEx" wide ascii nocase
    $o4 = "pSid2" wide ascii nocase
  condition:
    4 of ($o*)
}