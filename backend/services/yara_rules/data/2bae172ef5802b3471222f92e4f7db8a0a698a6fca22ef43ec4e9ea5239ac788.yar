rule auto_rule_20250726092248_6897 {
  strings:
    $o0 = "main_loop_entrance" wide ascii nocase
    $o1 = "dword_416F08" wide ascii nocase
    $o2 = "UnwindUp5_0" wide ascii nocase
  condition:
    3 of ($o*)
}