rule auto_rule_20250726102944_6524 {
  strings:
    $o0 = "dword_456018" wide ascii nocase
    $o1 = "xFF000000" wide ascii nocase
    $o2 = "dword_46ED38" wide ascii nocase
    $o3 = "tail_loop_start" wide ascii nocase
  condition:
    4 of ($o*)
}