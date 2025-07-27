rule auto_rule_20250726221118_8582 {
  strings:
    $o0 = "byte_4060D4" wide ascii nocase
    $o1 = "dword_45AFC8" wide ascii nocase
    $o2 = "_setenvp" wide ascii nocase
    $o3 = "dword_45B16C" wide ascii nocase
    $o4 = "main_loop_entrance" wide ascii nocase
  condition:
    4 of ($o*)
}