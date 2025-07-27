rule auto_rule_20250726171618_5864 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "asc_1EC82" wide ascii nocase
    $o2 = "dword_781A8" wide ascii nocase
    $o3 = "dword_7818C" wide ascii nocase
  condition:
    4 of ($o*)
}