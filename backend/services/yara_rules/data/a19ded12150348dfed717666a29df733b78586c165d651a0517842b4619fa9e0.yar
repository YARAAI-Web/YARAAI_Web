rule auto_rule_20250726103635_7756 {
  strings:
    $o0 = "_ShrMan" wide ascii nocase
    $o1 = "word_4474DC" wide ascii nocase
    $o2 = "dword_447A30" wide ascii nocase
    $o3 = "a_env" wide ascii nocase
  condition:
    4 of ($o*)
}