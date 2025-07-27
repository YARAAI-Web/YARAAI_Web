rule auto_rule_20250727032150_2064 {
  strings:
    $o0 = "dword_465470" wide ascii nocase
    $o1 = "_aullrem" wide ascii nocase
    $o2 = "_CrtMemCheckPoint" wide ascii nocase
    $o3 = "finish_loop" wide ascii nocase
  condition:
    4 of ($o*)
}