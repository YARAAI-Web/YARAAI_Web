rule auto_rule_20250727013257_6920 {
  strings:
    $o0 = "dword_44C8E4" wide ascii nocase
    $o1 = "dword_44C7A0" wide ascii nocase
    $o2 = "algn_44C692" wide ascii nocase
    $o3 = "_NLG_Notify1" wide ascii nocase
    $o4 = "InitializeCriticalSec" wide ascii nocase
  condition:
    4 of ($o*)
}