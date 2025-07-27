rule auto_rule_20250727024238_8618 {
  strings:
    $o0 = "UnwindUp3_0" wide ascii nocase
    $o1 = "dword_45AA1C" wide ascii nocase
    $o2 = "_wincmdln" wide ascii nocase
    $o3 = "dword_45B484" wide ascii nocase
    $o4 = "dword_45B15C" wide ascii nocase
  condition:
    4 of ($o*)
}