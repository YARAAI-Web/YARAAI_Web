#include "dd4968d3-4432-4e48-b953-7c2af03ad5be.h"

HRESULT __stdcall StringCchCopyA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc)
{
  HRESULT v3; // r9d
  size_t v4; // r10
  signed __int64 v5; // r8
  char v6; // al
  STRSAFE_LPSTR v7; // rax

  v3 = 0;
  if ( cchDest - 1 > 0x7FFFFFFE )
    v3 = -2147024809;
  if ( v3 < 0 )
  {
    if ( cchDest )
      *pszDest = 0;
  }
  else
  {
    if ( cchDest )
    {
      v4 = 2147483646 - cchDest;
      v5 = pszSrc - pszDest;
      do
      {
        if ( !(v4 + cchDest) )
          break;
        v6 = pszDest[v5];
        if ( !v6 )
          break;
        *pszDest++ = v6;
        --cchDest;
      }
      while ( cchDest );
    }
    v7 = pszDest - 1;
    if ( cchDest )
      v7 = pszDest;
    v3 = cchDest == 0 ? 0x8007007A : 0;
    *v7 = 0;
  }
  return v3;
}


HRESULT __stdcall StringCchCatA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc)
{
  HRESULT v3; // r9d
  size_t v7; // rcx
  STRSAFE_LPSTR i; // rax
  size_t v9; // r8
  char *v10; // rdx
  size_t v11; // rcx
  __int64 v12; // r9
  const char *v13; // r11
  char v14; // al
  char *v15; // rax

  v3 = 0;
  if ( cchDest - 1 > 0x7FFFFFFE )
    v3 = -2147024809;
  if ( v3 < 0 )
    goto LABEL_9;
  v7 = cchDest;
  for ( i = pszDest; v7; --v7 )
  {
    if ( !*i )
      break;
    ++i;
  }
  v3 = v7 == 0 ? 0x80070057 : 0;
  if ( v7 )
    v9 = cchDest - v7;
  else
LABEL_9:
    v9 = 0;
  if ( v3 >= 0 )
  {
    v10 = &pszDest[v9];
    v11 = cchDest - v9;
    if ( cchDest != v9 )
    {
      v12 = 2147483646;
      v13 = (const char *)(pszSrc - v10);
      do
      {
        if ( !v12 )
          break;
        v14 = v10[(_QWORD)v13];
        if ( !v14 )
          break;
        *v10 = v14;
        --v12;
        ++v10;
        --v11;
      }
      while ( v11 );
    }
    v15 = v10 - 1;
    if ( v11 )
      v15 = v10;
    v3 = v11 == 0 ? 0x8007007A : 0;
    *v15 = 0;
  }
  return v3;
}


HRESULT StringCchPrintfA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszFormat, ...)
{
  HRESULT v3; // edi
  size_t v5; // rbx
  int v6; // eax
  va_list ArgList; // [rsp+58h] [rbp+20h] BYREF

  va_start(ArgList, pszFormat);
  v3 = 0;
  if ( cchDest - 1 > 0x7FFFFFFE )
    v3 = -2147024809;
  if ( v3 < 0 )
  {
    if ( cchDest )
      *pszDest = 0;
  }
  else
  {
    v5 = cchDest - 1;
    v3 = 0;
    v6 = _vsnprintf(pszDest, cchDest - 1, pszFormat, ArgList);
    if ( v6 < 0 || v6 > v5 )
    {
      pszDest[v5] = 0;
      return -2147024774;
    }
    else if ( v6 == v5 )
    {
      pszDest[v5] = 0;
    }
  }
  return v3;
}


__int64 __fastcall CheckToken(_DWORD *a1)
{
  unsigned int v2; // edi
  HMODULE LibraryA; // rax
  HMODULE v4; // rbx
  FARPROC ProcAddress; // rsi
  PSID pSid; // [rsp+60h] [rbp-38h] BYREF
  _SID_IDENTIFIER_AUTHORITY pIdentifierAuthority; // [rsp+68h] [rbp-30h] BYREF

  *(_WORD *)&pIdentifierAuthority.Value[4] = 1280;
  v2 = 0;
  *(_DWORD *)pIdentifierAuthority.Value = 0;
  LibraryA = LoadLibraryA("advapi32.dll");
  v4 = LibraryA;
  if ( LibraryA )
  {
    ProcAddress = GetProcAddress(LibraryA, "CheckTokenMembership");
    if ( ProcAddress )
    {
      *a1 = 0;
      v2 = 1;
      if ( AllocateAndInitializeSid(&pIdentifierAuthority, 2u, 0x20u, 0x220u, 0, 0, 0, 0, 0, 0, &pSid) )
      {
        ((void (__fastcall *)(_QWORD, PSID, _DWORD *))ProcAddress)(0, pSid, a1);
        FreeSid(pSid);
      }
    }
    FreeLibrary(v4);
  }
  return v2;
}


BOOL __stdcall IsNTAdmin(DWORD dwReserved, DWORD *lpdwReserved)
{
  BOOL result; // eax
  HANDLE CurrentProcess; // rax
  _DWORD *v4; // rdi
  int v5; // esi
  int v6; // ecx
  BOOL v7; // [rsp+68h] [rbp+27h] BYREF
  DWORD TokenInformationLength; // [rsp+6Ch] [rbp+2Bh] BYREF
  HANDLE TokenHandle; // [rsp+70h] [rbp+2Fh] BYREF
  PSID pSid2; // [rsp+78h] [rbp+37h] BYREF
  struct _SID_IDENTIFIER_AUTHORITY pIdentifierAuthority; // [rsp+80h] [rbp+3Fh] BYREF

  result = dword_14000C14C;
  *(_DWORD *)pIdentifierAuthority.Value = 0;
  *(_WORD *)&pIdentifierAuthority.Value[4] = 1280;
  v7 = 0;
  if ( dword_14000C14C == 2 )
  {
    if ( (unsigned int)CheckToken(&v7) )
    {
      v6 = dword_14000C14C;
      result = v7;
      if ( v7 )
        v6 = 1;
      dword_14000C14C = v6;
    }
    else
    {
      CurrentProcess = GetCurrentProcess();
      result = OpenProcessToken(CurrentProcess, 8u, &TokenHandle);
      if ( result )
      {
        if ( !GetTokenInformation(TokenHandle, TokenGroups, 0, 0, &TokenInformationLength) && GetLastError() == 122 )
        {
          v4 = LocalAlloc(0, TokenInformationLength);
          if ( v4 )
          {
            if ( GetTokenInformation(TokenHandle, TokenGroups, v4, TokenInformationLength, &TokenInformationLength)
              && AllocateAndInitializeSid(&pIdentifierAuthority, 2u, 0x20u, 0x220u, 0, 0, 0, 0, 0, 0, &pSid2) )
            {
              v5 = 0;
              if ( *v4 )
              {
                while ( !EqualSid(*(PSID *)&v4[4 * v5 + 2], pSid2) )
                {
                  if ( (unsigned int)++v5 >= *v4 )
                    goto LABEL_14;
                }
                dword_14000C14C = 1;
                v7 = 1;
              }
LABEL_14:
              FreeSid(pSid2);
            }
            LocalFree(v4);
          }
        }
        CloseHandle(TokenHandle);
        return v7;
      }
    }
  }
  return result;
}


__int64 __fastcall WarningDlgProc(HWND hDlg, int a2, INT_PTR a3, UINT a4)
{
  int v6; // edx
  HWND DesktopWindow; // rax
  CHAR Buffer[512]; // [rsp+20h] [rbp-218h] BYREF

  v6 = a2 - 272;
  if ( v6 )
  {
    if ( v6 != 1 || (unsigned __int64)(a3 - 2109) > 1 )
      return 0;
    EndDialog(hDlg, a3);
  }
  else
  {
    DesktopWindow = GetDesktopWindow();
    CenterWindow(hDlg, DesktopWindow);
    Buffer[0] = 0;
    LoadStringA(g_hInst, a4, Buffer, 512);
    SetDlgItemTextA(hDlg, 2111, Buffer);
    MessageBeep(0xFFFFFFFF);
  }
  return 1;
}


_BYTE *__fastcall ExtractField(_BYTE **a1, const CHAR *a2)
{
  _BYTE *v2; // rbx
  int v5; // ebp
  _BYTE *v6; // rdi
  _BYTE *result; // rax

  v2 = *a1;
  v5 = 0;
  while ( ANSIStrChr(a2) )
  {
    if ( !*v2 )
      return 0;
    ++v2;
  }
  *a1 = v2;
  if ( !ANSIStrChr(a2) )
  {
    v6 = v2;
    do
    {
      if ( !*v6 )
        break;
      ++v6;
      ++v5;
    }
    while ( !ANSIStrChr(a2) );
  }
  result = &v2[v5];
  if ( *result )
    *result++ = 0;
  return result;
}


__int64 __fastcall AnalyzeCmd(STRSAFE_LPSTR pszDest, __int64 a2, char **a3, _DWORD *a4)
{
  char *v6; // rcx
  __int64 v7; // r10
  __int64 v10; // rdx
  char v11; // al
  char *v12; // rax
  const CHAR *v13; // rdx
  const CHAR *v14; // rax
  const CHAR *Field; // rax
  const char *v16; // rdi
  __int64 v17; // rbx
  const CHAR *v18; // rsi
  unsigned __int64 v19; // rax
  CHAR v20; // al
  signed __int64 v21; // r8
  SIZE_T *v22; // rcx
  __int64 v23; // rdx
  char v24; // al
  SIZE_T *v25; // rax
  __int64 v26; // rdx
  SIZE_T *v27; // rcx
  char v28; // al
  SIZE_T *v29; // rax
  const CHAR *v30; // rax
  DWORD FileAttributesA; // eax
  const CHAR *v32; // rcx
  const CHAR *v33; // rax
  char *v34; // rbx
  LPCSTR v35; // rsi
  const char *v36; // rdi
  const CHAR *v37; // rcx
  UINT PrivateProfileIntA; // eax
  const char *v39; // r14
  const CHAR *v41; // rax
  __int64 v42; // rax
  __int64 v43; // rdi
  char *v44; // rax
  __int64 v45; // rdi
  DWORD v46; // eax
  __int64 v47; // rdx
  char *v48; // rcx
  char v49; // al
  char *v50; // rax
  __int64 v51; // r14
  char *v52; // rdx
  char v53; // al
  char *v54; // rcx
  LPCSTR lpAppName[2]; // [rsp+30h] [rbp-D0h] BYREF
  SIZE_T FileName[34]; // [rsp+40h] [rbp-C0h] BYREF
  char v57; // [rsp+150h] [rbp+50h] BYREF
  char v58; // [rsp+151h] [rbp+51h] BYREF
  char pszDesta[1024]; // [rsp+260h] [rbp+160h] BYREF

  v6 = &v57;
  v7 = pszDest - &v57;
  v10 = 260;
  do
  {
    if ( v10 == -2147483386 )
      break;
    v11 = v6[v7];
    if ( !v11 )
      break;
    *v6++ = v11;
    --v10;
  }
  while ( v10 );
  v12 = v6 - 1;
  if ( v10 )
    v12 = v6;
  *v12 = 0;
  if ( v57 == 34 )
  {
    v13 = "\"";
    v14 = &v58;
  }
  else
  {
    v13 = " ";
    v14 = &v57;
  }
  lpAppName[0] = v14;
  Field = ExtractField((_BYTE **)lpAppName, v13);
  v16 = lpAppName[0];
  v17 = -1;
  v18 = Field;
  if ( !lpAppName[0] )
    goto LABEL_25;
  v19 = -1;
  do
    ++v19;
  while ( lpAppName[0][v19] );
  if ( v19 < 3 )
    goto LABEL_25;
  if ( (v20 = lpAppName[0][1], v20 == 58) && lpAppName[0][2] == 92 || *lpAppName[0] == 92 && v20 == 92 )
  {
    v21 = lpAppName[0] - (LPCSTR)FileName;
    v22 = FileName;
    v23 = 260;
    do
    {
      if ( v23 == -2147483386 )
        break;
      v24 = *((_BYTE *)v22 + v21);
      if ( !v24 )
        break;
      *(_BYTE *)v22 = v24;
      v22 = (SIZE_T *)((char *)v22 + 1);
      --v23;
    }
    while ( v23 );
    v25 = (SIZE_T *)((char *)v22 - 1);
    if ( v23 )
      v25 = v22;
    *(_BYTE *)v25 = 0;
  }
  else
  {
LABEL_25:
    v26 = 260;
    v27 = FileName;
    do
    {
      if ( v26 == -2147483386 )
        break;
      v28 = *((_BYTE *)v27 + &PathName - (CHAR *)FileName);
      if ( !v28 )
        break;
      *(_BYTE *)v27 = v28;
      v27 = (SIZE_T *)((char *)v27 + 1);
      --v26;
    }
    while ( v26 );
    v29 = (SIZE_T *)((char *)v27 - 1);
    if ( v26 )
      v29 = v27;
    *(_BYTE *)v29 = 0;
    AddPath((STRSAFE_LPSTR)FileName, 0x104u, v16);
  }
  v30 = (const CHAR *)ANSIStrRChr(v16);
  if ( v30 && CompareStringA(0x7Fu, 1u, v30, -1, ".INF", -1) == 2 )
  {
    FileAttributesA = GetFileAttributesA((LPCSTR)FileName);
    if ( FileAttributesA != -1 && (FileAttributesA & 0x10) == 0 )
    {
      lpAppName[0] = v18;
      v32 = ExtractField((_BYTE **)lpAppName, "[");
      if ( v32 )
      {
        v33 = lpAppName[0];
        if ( *v32 )
          v33 = v32;
        lpAppName[0] = v33;
        ExtractField((_BYTE **)lpAppName, "]");
      }
      v34 = (char *)LocalAlloc(0x40u, 0x200u);
      if ( v34 )
      {
        v35 = lpAppName[0];
        v36 = aDefaultinstall;
        v37 = aDefaultinstall;
        if ( *lpAppName[0] )
          v37 = lpAppName[0];
        PrivateProfileIntA = GetPrivateProfileIntA(v37, "Reboot", 0, (LPCSTR)FileName);
        *a4 = 1;
        g_uInfRebootOn = PrivateProfileIntA;
        if ( GetPrivateProfileStringA("Version", "AdvancedINF", pszCabPath, v34, 8u, (LPCSTR)FileName) )
        {
          dword_14000DE64 |= 4u;
          if ( *v35 )
            v36 = v35;
          StringCchCopyA(pszDest, 0x104u, v36);
          StringCchCopyA(v34, 0x200u, (STRSAFE_LPCSTR)FileName);
        }
        else
        {
          dword_14000DE64 &= ~4u;
          if ( g_wOSVer )
          {
            v39 = "setupapi.dll";
          }
          else
          {
            v39 = "setupx.dll";
            GetShortPathNameA((LPCSTR)FileName, (LPSTR)FileName, 0x104u);
          }
          if ( *v35 )
            v36 = v35;
          StringCchPrintfA(v34, 0x200u, pszFormat, v39, v36, FileName);
        }
        goto LABEL_82;
      }
    }
LABEL_53:
    MsgBox2Param(0, 0x10u, 0);
    return 0;
  }
  v41 = (const CHAR *)ANSIStrRChr(v16);
  if ( !v41 || CompareStringA(0x7Fu, 1u, v41, -1, ".BAT", -1) != 2 )
  {
    v45 = 1024;
    v34 = (char *)LocalAlloc(0x40u, 0x400u);
    if ( v34 )
    {
      v46 = GetFileAttributesA((LPCSTR)FileName);
      if ( v46 == -1 || (v46 & 0x10) != 0 )
      {
        v51 = pszDest - pszDesta;
        v52 = pszDesta;
        do
        {
          if ( v45 == -2147482622 )
            break;
          v53 = v52[v51];
          if ( !v53 )
            break;
          *v52++ = v53;
          --v45;
        }
        while ( v45 );
        v54 = v52 - 1;
        if ( v45 )
          v54 = v52;
        *v54 = 0;
      }
      else
      {
        v47 = 1024;
        v48 = pszDesta;
        do
        {
          if ( v47 == -2147482622 )
            break;
          v49 = v48[(char *)FileName - pszDesta];
          if ( !v49 )
            break;
          *v48++ = v49;
          --v47;
        }
        while ( v47 );
        v50 = v48 - 1;
        if ( v47 )
          v50 = v48;
        *v50 = 0;
        if ( v18 && *v18 )
        {
          StringCchCatA(pszDesta, 0x400u, " ");
          StringCchCatA(pszDesta, 0x400u, v18);
        }
      }
      *v34 = 0;
      ExpandCmdParams(pszDesta);
      goto LABEL_82;
    }
    goto LABEL_53;
  }
  v42 = -1;
  do
    ++v42;
  while ( aCommandComCS[v42] );
  do
    ++v17;
  while ( *((_BYTE *)FileName + v17) );
  v43 = v42 + v17;
  v44 = (char *)LocalAlloc(0x40u, v42 + v17 + 8);
  v34 = v44;
  if ( !v44 )
    goto LABEL_53;
  StringCchPrintfA(v44, v43 + 8, "Command.com /c %s", (const char *)FileName);
LABEL_82:
  *a3 = v34;
  return 1;
}


__int64 MyNTReboot()
{
  HANDLE CurrentProcess; // rax
  BOOL v2; // ebx
  HANDLE TokenHandle; // [rsp+30h] [rbp-28h] BYREF
  _TOKEN_PRIVILEGES NewState; // [rsp+38h] [rbp-20h] BYREF

  CurrentProcess = GetCurrentProcess();
  if ( OpenProcessToken(CurrentProcess, 0x28u, &TokenHandle) )
  {
    LookupPrivilegeValueA(0, "SeShutdownPrivilege", &NewState.Privileges[0].Luid);
    NewState.PrivilegeCount = 1;
    NewState.Privileges[0].Attributes = 2;
    v2 = AdjustTokenPrivileges(TokenHandle, 0, &NewState, 0, 0, 0);
    CloseHandle(TokenHandle);
    if ( v2 )
    {
      if ( ExitWindowsEx(2u, 0) )
        return 1;
    }
  }
  MsgBox2Param(0, 0x10u, 0);
  return 0;
}


unsigned int AddRegRunOnce()
{
  int v0; // r14d
  unsigned int result; // eax
  int i; // ebx
  HMODULE LibraryA; // rax
  HMODULE v4; // rdi
  FARPROC ProcAddress; // rbx
  __int64 v6; // rbx
  __int64 v7; // rax
  __int64 v8; // rcx
  SIZE_T v9; // rsi
  char *lpData; // rdi
  const char *v11; // r8
  HKEY hKey; // [rsp+58h] [rbp-B0h] BYREF
  DWORD dwDisposition; // [rsp+60h] [rbp-A8h] BYREF
  DWORD cbData; // [rsp+64h] [rbp-A4h] BYREF
  CHAR Filename[272]; // [rsp+68h] [rbp-A0h] BYREF
  CHAR Buffer[272]; // [rsp+178h] [rbp+70h] BYREF

  memset_0(Filename, 0, 0x104u);
  memset_0(Buffer, 0, 0x104u);
  v0 = 0;
  result = RegCreateKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0, 0, 0x2001Fu, 0, &hKey, &dwDisposition);
  if ( !result )
  {
    for ( i = 0; i < 200; ++i )
    {
      StringCchPrintfA(g_szRegValName, 0x50u, "wextract_cleanup%d", i);
      if ( RegQueryValueExA(hKey, g_szRegValName, 0, 0, 0, &cbData) )
        break;
    }
    if ( i == 200 )
    {
      result = RegCloseKey(hKey);
      g_szRegValName[0] = 0;
      return result;
    }
    GetSystemDirectoryA(Buffer, 0x104u);
    AddPath(Buffer, 0x104u, "advpack.dll");
    LibraryA = LoadLibraryA(Buffer);
    v4 = LibraryA;
    if ( LibraryA
      && (ProcAddress = GetProcAddress(LibraryA, "DelNodeRunDLL32"),
          LOBYTE(v0) = ProcAddress != 0,
          FreeLibrary(v4),
          ProcAddress) )
    {
      if ( GetSystemDirectoryA(Filename, 0x104u) )
        AddPath(Filename, 0x104u, pszCabPath);
    }
    else if ( !GetModuleFileNameA(g_hInst, Filename, 0x104u) )
    {
      return RegCloseKey(hKey);
    }
    v6 = -1;
    v7 = -1;
    do
      ++v7;
    while ( *(&PathName + v7) );
    v8 = -1;
    do
      ++v8;
    while ( Filename[v8] );
    v9 = (unsigned int)(v8 + v7 + 80);
    lpData = (char *)LocalAlloc(0x40u, v9);
    if ( !lpData )
    {
      MsgBox2Param(0, 0x10u, 0);
      return RegCloseKey(hKey);
    }
    v11 = aSDS;
    g_bConvertRunOnce = v0 ^ 1;
    if ( v0 )
      v11 = aRundll32ExeSad;
    StringCchPrintfA(lpData, v9, v11, Filename, &PathName);
    do
      ++v6;
    while ( lpData[v6] );
    RegSetValueExA(hKey, g_szRegValName, 0, 1u, (const BYTE *)lpData, v6 + 1);
    RegCloseKey(hKey);
    return (unsigned int)LocalFree(lpData);
  }
  return result;
}


void __fastcall DeleteMyDir(const CHAR *a1)
{
  char *v2; // rcx
  __int64 v3; // rdx
  signed __int64 v4; // rbx
  char v5; // al
  char *v6; // rax
  HANDLE FirstFileA; // rsi
  __int64 v8; // r8
  char *v9; // rdx
  char v10; // al
  char *v11; // rax
  bool v12; // zf
  _WIN32_FIND_DATAA FindFileData; // [rsp+20h] [rbp-E0h] BYREF
  char pszDest[272]; // [rsp+160h] [rbp+60h] BYREF

  if ( *a1 )
  {
    v2 = pszDest;
    v3 = 260;
    v4 = a1 - pszDest;
    do
    {
      if ( v3 == -2147483386 )
        break;
      v5 = v2[v4];
      if ( !v5 )
        break;
      *v2++ = v5;
      --v3;
    }
    while ( v3 );
    v6 = v2 - 1;
    if ( v3 )
      v6 = v2;
    *v6 = 0;
    StringCchCatA(pszDest, 0x104u, "*");
    FirstFileA = FindFirstFileA(pszDest, &FindFileData);
    if ( FirstFileA != (HANDLE)-1LL )
    {
      do
      {
        v8 = 260;
        v9 = pszDest;
        do
        {
          if ( v8 == -2147483386 )
            break;
          v10 = v9[v4];
          if ( !v10 )
            break;
          *v9++ = v10;
          --v8;
        }
        while ( v8 );
        v11 = v9 - 1;
        if ( v8 )
          v11 = v9;
        v12 = (FindFileData.dwFileAttributes & 0x10) == 0;
        *v11 = 0;
        if ( v12 )
        {
          StringCchCatA(pszDest, 0x104u, FindFileData.cFileName);
          SetFileAttributesA(pszDest, 0x80u);
          DeleteFileA(pszDest);
        }
        else if ( lstrcmpA(FindFileData.cFileName, ".") )
        {
          if ( lstrcmpA(FindFileData.cFileName, "..") )
          {
            StringCchCatA(pszDest, 0x104u, FindFileData.cFileName);
            AddPath(pszDest, 0x104u, pszCabPath);
            DeleteMyDir(pszDest);
          }
        }
      }
      while ( FindNextFileA(FirstFileA, &FindFileData) );
      FindClose(FirstFileA);
      RemoveDirectoryA(a1);
    }
  }
}


__int64 GetWininitSize()
{
  unsigned int v0; // ebx
  HFILE v1; // eax
  HFILE v2; // edi
  CHAR Buffer[272]; // [rsp+20h] [rbp-128h] BYREF

  v0 = 0;
  if ( GetWindowsDirectoryA(Buffer, 0x104u) )
  {
    AddPath(Buffer, 0x104u, "wininit.ini");
    WritePrivateProfileStringA(0, 0, 0, Buffer);
    v1 = _lopen(Buffer, 64);
    v2 = v1;
    if ( v1 != -1 )
    {
      v0 = _llseek(v1, 0, 2);
      _lclose(v2);
    }
  }
  return v0;
}


DWORD __stdcall NeedRebootInit()
{
  unsigned __int16 v0; // cx
  DWORD v1; // ebx
  LSTATUS v2; // eax
  DWORD v3; // ecx
  DWORD cbData; // [rsp+70h] [rbp+10h] BYREF
  HKEY hKey; // [rsp+78h] [rbp+18h] BYREF

  v1 = 0;
  if ( !v0 )
    return GetWininitSize();
  if ( v0 == 1 )
  {
    cbData = 0;
    if ( !RegOpenKeyExA(HKEY_LOCAL_MACHINE, aSystemCurrentc_0, 0, 0x20019u, &hKey) )
    {
      v2 = RegQueryInfoKeyA(hKey, 0, 0, 0, 0, 0, 0, &cbData, 0, 0, 0, 0);
      goto LABEL_6;
    }
    return cbData;
  }
  if ( v0 <= 3u )
  {
    cbData = 0;
    if ( !RegOpenKeyExA(HKEY_LOCAL_MACHINE, aSystemCurrentc, 0, 0x20019u, &hKey) )
    {
      v2 = RegQueryValueExA(hKey, ValueName, 0, 0, 0, &cbData);
LABEL_6:
      v3 = cbData;
      if ( v2 )
        v3 = 0;
      cbData = v3;
      RegCloseKey(hKey);
      return cbData;
    }
    return cbData;
  }
  return v1;
}


__int64 __fastcall IsWindowsDrive(_BYTE *a1)
{
  unsigned int v2; // ebx
  SIZE_T Buffer; // [rsp+30h] [rbp-128h] BYREF

  v2 = 0;
  if ( !GetWindowsDirectoryA((LPSTR)&Buffer, 0x104u) )
    MsgBox2Param(0, 0x10u, 0);
  LOBYTE(v2) = *a1 == (unsigned __int8)Buffer;
  return v2;
}


__int64 __fastcall DiskSpaceErrMsg(int a1, int a2, int a3)
{
  unsigned int v3; // ebx
  char pszDest[16]; // [rsp+30h] [rbp-28h] BYREF

  v3 = 0;
  g_dwExitCode = 112;
  switch ( a1 )
  {
    case 1:
      StringCchPrintfA(pszDest, 0xAu, "%lu", a3 + a2);
      MsgBox2Param(0, 0x10u, 0);
      break;
    case 4:
      StringCchPrintfA(pszDest, 0xAu, "%lu", a3 + a2);
      LOBYTE(v3) = (unsigned int)MsgBox2Param(0, 0x20u, 5) == 4;
      break;
    case 2:
      StringCchPrintfA(pszDest, 0xAu, "%lu", a3);
      if ( (unsigned int)MsgBox2Param(0, 0x40u, 260) == 6 )
      {
        g_dwExitCode = 0;
        return 1;
      }
      break;
  }
  return v3;
}


__int64 __fastcall GetFileTobeChecked(LPSTR lpBuffer, __int64 a2, const char *a3)
{
  int v3; // edi
  const char *v4; // rsi
  CHAR *v5; // rbx
  const CHAR *v6; // rsi
  unsigned __int8 v7; // r14
  const CHAR *v8; // rax
  __int64 v9; // rdx
  CHAR *v10; // rcx
  CHAR v11; // al
  CHAR *v12; // rax
  DWORD v13; // eax
  DWORD Type; // [rsp+30h] [rbp-D0h] BYREF
  DWORD cbData; // [rsp+34h] [rbp-CCh] BYREF
  HKEY hKey; // [rsp+38h] [rbp-C8h] BYREF
  CHAR SubKey[272]; // [rsp+40h] [rbp-C0h] BYREF

  v3 = 0;
  v4 = a3;
  *lpBuffer = 0;
  v5 = lpBuffer;
  if ( *a3 == 35 )
  {
    v6 = a3 + 1;
    v7 = (unsigned __int8)CharUpperA((LPSTR)a3[1]);
    v8 = CharNextA(v6);
    v4 = CharNextA(v8);
    if ( v7 != 83 )
    {
      if ( v7 == 87 )
      {
        GetWindowsDirectoryA(v5, 0x104u);
LABEL_23:
        AddPath(v5, 0x104u, v4);
        return 1;
      }
      cbData = 260;
      v9 = 260;
      v10 = SubKey;
      do
      {
        if ( v9 == -2147483386 )
          break;
        v11 = v10["Software\\Microsoft\\Windows\\CurrentVersion\\App Paths" - SubKey];
        if ( !v11 )
          break;
        *v10++ = v11;
        --v9;
      }
      while ( v9 );
      v12 = v10 - 1;
      if ( v9 )
        v12 = v10;
      *v12 = 0;
      AddPath(SubKey, 0x104u, v4);
      if ( RegOpenKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0x20019u, &hKey) )
        goto LABEL_23;
      if ( RegQueryValueExA(hKey, pszCabPath, 0, &Type, (LPBYTE)v5, &cbData) )
        goto LABEL_18;
      v13 = Type;
      if ( Type == 2 )
      {
        if ( ExpandEnvironmentStringsA(v5, SubKey, 0x104u) )
        {
          StringCchCopyA(v5, 0x104u, SubKey);
          v3 = 1;
LABEL_18:
          RegCloseKey(hKey);
          goto LABEL_22;
        }
        v13 = Type;
      }
      if ( v13 == 1 )
        v3 = 1;
      goto LABEL_18;
    }
    lpBuffer = v5;
  }
  GetSystemDirectoryA(lpBuffer, 0x104u);
LABEL_22:
  if ( !v3 )
    goto LABEL_23;
  return 1;
}


__int64 __fastcall CheckFileVersion(__int64 a1, const CHAR *a2, DWORD a3, _DWORD *a4)
{
  CHAR *v4; // rsi
  void *v6; // rbx
  unsigned int v7; // r13d
  int v8; // r12d
  __int64 v9; // rax
  __int64 v10; // rdi
  DWORD FileVersionInfoSizeA; // eax
  DWORD v12; // esi
  HGLOBAL v13; // rax
  void *v14; // rax
  const void *v15; // r14
  DWORD v16; // r8d
  unsigned int *v17; // rcx
  __int64 v18; // rdx
  unsigned int v19; // r9d
  unsigned int v20; // r8d
  int v21; // eax
  int v22; // eax
  _DWORD v24[2]; // [rsp+20h] [rbp-28h]
  _DWORD v25[2]; // [rsp+28h] [rbp-20h]
  __int64 v26; // [rsp+30h] [rbp-18h]
  LPVOID lpBuffer; // [rsp+38h] [rbp-10h] BYREF
  unsigned int puLen; // [rsp+90h] [rbp+48h] BYREF
  LPCSTR lptstrFilename; // [rsp+98h] [rbp+50h]
  DWORD dwHandle; // [rsp+A0h] [rbp+58h] BYREF
  _DWORD *v31; // [rsp+A8h] [rbp+60h]

  v31 = a4;
  dwHandle = a3;
  lptstrFilename = a2;
  v4 = (CHAR *)a2;
  v6 = 0;
  v7 = 0;
  v8 = 0;
  if ( *(int *)(a1 + 124) <= 0 )
    goto LABEL_34;
  v9 = 0;
  v26 = 0;
  while ( 1 )
  {
    v10 = v9 + *(unsigned int *)(a1 + 128);
    if ( !(unsigned int)GetFileTobeChecked(
                          v4,
                          (__int64)a2,
                          (const char *)(*(unsigned int *)(v10 + a1 + 188) + a1 + 132)) )
      goto LABEL_35;
    FileVersionInfoSizeA = GetFileVersionInfoSizeA(v4, &dwHandle);
    v12 = FileVersionInfoSizeA;
    if ( !FileVersionInfoSizeA )
      break;
    v13 = GlobalAlloc(0x42u, FileVersionInfoSizeA);
    v6 = v13;
    if ( !v13 )
      goto LABEL_35;
    v14 = GlobalLock(v13);
    v15 = v14;
    if ( !v14 )
      goto LABEL_35;
    v16 = v12;
    v4 = (CHAR *)lptstrFilename;
    if ( !GetFileVersionInfoA(lptstrFilename, dwHandle, v16, v14)
      || !VerQueryValueA(v15, "\\", &lpBuffer, &puLen)
      || !puLen )
    {
      goto LABEL_29;
    }
    v17 = (unsigned int *)(v10 + a1 + 144);
    v18 = 0;
    v19 = *((_DWORD *)lpBuffer + 3);
    v20 = *((_DWORD *)lpBuffer + 2);
    do
    {
      if ( v20 < *(v17 - 3) )
      {
LABEL_12:
        v21 = -1;
        goto LABEL_17;
      }
      if ( v20 <= *(v17 - 3) )
      {
        if ( v19 < *(v17 - 2) )
          goto LABEL_12;
        v21 = v19 > *(v17 - 2);
      }
      else
      {
        v21 = 1;
      }
LABEL_17:
      v24[v18] = v21;
      if ( v20 < *v17 )
        goto LABEL_18;
      if ( v20 <= *v17 )
      {
        if ( v19 < v17[1] )
        {
LABEL_18:
          v22 = -1;
          goto LABEL_23;
        }
        v22 = v19 > v17[1];
      }
      else
      {
        v22 = 1;
      }
LABEL_23:
      v25[v18] = v22;
      v17 += 6;
      ++v18;
    }
    while ( v18 < 2 );
    if ( (v24[0] < 0 || v25[0] > 0) && (v24[1] < 0 || v25[1] > 0) )
    {
      GlobalUnlock(v6);
      goto LABEL_35;
    }
LABEL_29:
    GlobalUnlock(v6);
LABEL_33:
    ++v8;
    v9 = v26 + 60;
    v26 += 60;
    if ( v8 >= *(_DWORD *)(a1 + 124) )
    {
LABEL_34:
      v7 = 1;
      goto LABEL_35;
    }
  }
  if ( !*(_DWORD *)(v10 + a1 + 132) && !*(_DWORD *)(v10 + a1 + 136) )
  {
    v4 = (CHAR *)lptstrFilename;
    goto LABEL_33;
  }
LABEL_35:
  *v31 = v8;
  if ( v6 )
    GlobalFree(v6);
  return v7;
}


void __fastcall ExpandCmdParams(CHAR *lpsz, unsigned __int64 a2, LPSTR a3)
{
  LPSTR v5; // rdi
  BYTE v6; // al
  BOOL v7; // eax
  __int64 v8; // rax
  LPSTR v9; // rax
  size_t v10; // rdx
  __int64 v11; // rax
  size_t v12; // rdx
  CHAR Filename[272]; // [rsp+20h] [rbp-138h] BYREF

  v5 = lpsz;
  if ( *lpsz )
  {
    GetModuleFileNameA(g_hInst, Filename, 0x104u);
    v6 = *v5;
    if ( *v5 )
    {
      while ( 1 )
      {
        v7 = IsDBCSLeadByte(v6);
        *a3 = *v5;
        if ( v7 )
          a3[1] = v5[1];
        if ( *v5 != 35 )
        {
LABEL_28:
          a3 = CharNextA(a3);
          goto LABEL_29;
        }
        v5 = CharNextA(v5);
        if ( (unsigned __int8)CharUpperA((LPSTR)*v5) == 68 )
          break;
        if ( (unsigned __int8)CharUpperA((LPSTR)*v5) == 69 )
        {
          if ( (unsigned __int64)a3 < a2 || (unsigned __int64)&a3[-a2] > 0x400 )
            v12 = 0;
          else
            v12 = a2 - (_QWORD)a3 + 1024;
          StringCchCopyA(a3, v12, Filename);
          v11 = -1;
          do
            ++v11;
          while ( a3[v11] );
LABEL_26:
          a3 += v11;
          goto LABEL_29;
        }
        if ( *v5 == 35 )
          goto LABEL_28;
LABEL_29:
        v5 = CharNextA(v5);
        v6 = *v5;
        if ( !*v5 )
          goto LABEL_30;
      }
      GetParentDir(Filename);
      v8 = -1;
      do
        ++v8;
      while ( Filename[v8] );
      v9 = CharPrevA(Filename, &Filename[v8]);
      if ( v9 && *v9 == 92 )
        *v9 = 0;
      if ( (unsigned __int64)a3 < a2 || (unsigned __int64)&a3[-a2] > 0x400 )
        v10 = 0;
      else
        v10 = a2 - (_QWORD)a3 + 1024;
      StringCchCopyA(a3, v10, Filename);
      v11 = -1;
      do
        ++v11;
      while ( a3[v11] );
      goto LABEL_26;
    }
LABEL_30:
    *a3 = 0;
  }
}


int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
  signed int Version; // eax
  HMODULE ModuleHandleW; // rax
  FARPROC ProcAddress; // rax
  int v8; // ebx
  char v9; // di
  int v10; // ebx

  Version = GetVersion();
  if ( Version >= 0 && (unsigned __int8)Version >= 6u )
  {
    ModuleHandleW = GetModuleHandleW(L"Kernel32.dll");
    if ( ModuleHandleW )
    {
      ProcAddress = GetProcAddress(ModuleHandleW, "HeapSetInformation");
      if ( ProcAddress )
        ((void (__fastcall *)(_QWORD, __int64, _QWORD, _QWORD))ProcAddress)(0, 1, 0, 0);
    }
  }
  g_dwExitCode = 0;
  if ( (unsigned int)Init(hInstance) )
  {
    v8 = DoMain();
    DeleteExtractedFiles();
    if ( v8 )
    {
      if ( !byte_14000CD1A )
      {
        v9 = dword_14000DE5C;
        if ( (dword_14000DE5C & 1) != 0 )
        {
          if ( (dword_14000DE5C & 2) != 0 || g_uInfRebootOn || (v10 = g_dwRebootCheck, v10 != NeedRebootInit()) )
          {
            if ( (v9 & 4) != 0 || (unsigned int)MsgBox2Param(0, 0x40u, 4) == 6 )
            {
              if ( g_wOSVer )
                MyNTReboot();
              else
                ExitWindowsEx(2u, 0);
            }
          }
        }
      }
    }
  }
  if ( g_hMutex )
    CloseHandle(g_hMutex);
  return g_dwExitCode;
}


__int64 __fastcall Init(HMODULE hModule, const CHAR *a2)
{
  HGLOBAL Resource; // rdi
  HRSRC ResourceA; // rax
  DWORD *v7; // rdx
  DWORD v8; // ecx
  __int64 v9; // rcx
  SIZE_T Name[34]; // [rsp+30h] [rbp-138h] BYREF

  g_hInst = hModule;
  Resource = 0;
  memset_0(&g_Sess, 0, 0x910u);
  memset_0(&g_CMD, 0, 0x32Cu);
  memset_0(&g_szBrowsePath, 0, 0x104u);
  dword_14000D818 = 1;
  if ( (unsigned int)GetResource("TITLE", Caption, 0x7Fu) - 1 > 0x7F )
    goto LABEL_31;
  g_hCancelEvent = CreateEventA(0, 1, 1, 0);
  SetEvent(g_hCancelEvent);
  if ( !(unsigned int)GetResource("EXTRACTOPT", &dword_14000DE64, 4u) )
  {
    MsgBox2Param(0, 0x10u, 0);
LABEL_4:
    g_dwExitCode = -2147023084;
    return 0;
  }
  if ( (dword_14000DE64 & 0x40) != 0 || (dword_14000DE64 & 0x80u) != 0 )
  {
    if ( !(unsigned int)GetResource("INSTANCECHECK", Name, 0x104u) )
    {
      MsgBox2Param(0, 0x10u, 0);
      goto LABEL_4;
    }
    g_hMutex = CreateMutexA(0, 1, (LPCSTR)Name);
    if ( g_hMutex )
    {
      if ( GetLastError() == 183 )
      {
        if ( (dword_14000DE64 & 0x80u) != 0 )
        {
          MsgBox2Param(0, 0x10u, 0);
LABEL_14:
          CloseHandle(g_hMutex);
          g_dwExitCode = -2147024713;
          return 0;
        }
        if ( (unsigned int)MsgBox2Param(0, 0x20u, 4) != 6 )
          goto LABEL_14;
      }
    }
  }
  g_uInfRebootOn = 0;
  if ( !(unsigned int)ParseCmdLine(a2) )
  {
LABEL_31:
    MsgBox2Param(0, 0x10u, 0);
    return 0;
  }
  if ( byte_14000CD1A[0] )
  {
    DeleteMyDir(byte_14000CD1A);
  }
  else
  {
    ResourceA = FindResourceA(hModule, "VERCHECK", (LPCSTR)0xA);
    if ( ResourceA )
      Resource = LoadResource(hModule, ResourceA);
    if ( g_fOSSupportsFullUI )
      InitCommonControls();
    if ( dword_14000CD04
      || (unsigned int)CheckOSVersion(Resource)
      && ((unsigned __int16)(g_wOSVer - 1) > 2u
       || (dword_14000DE64 & 0x100) == 0
       || (word_14000CD18 & 1) != 0
       || IsNTAdmin(v8, v7)
       || MyDialogBox(v9, 2006, 0, WarningDlgProc, 1351, 2110) == 2109) )
    {
      return 1;
    }
  }
  return 0;
}


__int64 DoMain()
{
  HMODULE LibraryA; // rax
  HMODULE v1; // rbx
  FARPROC ProcAddress; // rax
  _DWORD *v4; // rax
  __int64 v5; // rcx
  bool v6; // zf
  DWORD v7; // eax
  int v8; // eax
  SIZE_T Buffer[34]; // [rsp+30h] [rbp-238h] BYREF
  CHAR v10[272]; // [rsp+140h] [rbp-128h] BYREF

  if ( !word_14000CD18 )
  {
    if ( dword_14000CD04 )
      goto LABEL_43;
    if ( !(unsigned int)GetUsersPermission() )
      return 0;
    if ( !word_14000CD18 )
    {
LABEL_43:
      if ( (unsigned int)DisplayLicense() )
        goto LABEL_6;
      return 0;
    }
  }
LABEL_6:
  if ( !(unsigned int)GetFileList() || !(unsigned int)GetTempDirectory() )
    return 0;
  GetSystemDirectoryA((LPSTR)Buffer, 0x105u);
  AddPath((STRSAFE_LPSTR)Buffer, 0x105u, "advapi32.dll");
  LibraryA = LoadLibraryA((LPCSTR)Buffer);
  v1 = LibraryA;
  if ( LibraryA )
  {
    ProcAddress = GetProcAddress(LibraryA, "DecryptFileA");
    if ( ProcAddress )
      ((void (__fastcall *)(CHAR *, _QWORD))ProcAddress)(&PathName, 0);
  }
  FreeLibrary(v1);
  if ( !dword_14000CD04 && !dword_14000DE60 )
  {
    if ( !GetWindowsDirectoryA(v10, 0x104u) )
    {
LABEL_14:
      MsgBox2Param(0, 0x10u, 0);
      g_dwExitCode = MyGetLastError();
      return 0;
    }
    if ( !(unsigned int)IsEnoughSpace(v10) )
      return 0;
  }
  if ( !SetCurrentDirectoryA(&PathName) )
    goto LABEL_14;
  if ( !dword_14000CD0C )
  {
    v4 = &g_FileTable;
    v5 = 40;
    do
    {
      *v4 = 1;
      v4 += 8;
      --v5;
    }
    while ( v5 );
    if ( (word_14000CD18 & 1) != 0 || (dword_14000DE64 & 1) != 0 )
      v6 = ExtractThread(0).dwLowDateTime == 0;
    else
      v6 = MyDialogBox(0, 2005LL - (g_fOSSupportsFullUI != 0), 0, ExtractDlgProc, 0, 0) == 0;
    if ( v6 )
    {
      g_dwExitCode = -2147023829;
      return 0;
    }
    if ( !(unsigned int)TravelUpdatedFiles(ProcessUpdatedFile_Write) )
      return 0;
    g_dwExitCode = 0;
  }
  if ( (dword_14000D028 & 0x40) != 0 || (dword_14000D028 & 0x80u) != 0 )
    v7 = 0;
  else
    v7 = NeedRebootInit();
  g_dwRebootCheck = v7;
  v8 = dword_14000CD04;
  if ( !dword_14000CD04 && !dword_14000DE60 )
  {
    if ( !(unsigned int)RunInstallCommand() )
      return 0;
    v8 = dword_14000CD04;
  }
  if ( !word_14000CD18 && !v8 )
    FinishMessage();
  return 1;
}


LRESULT __fastcall MEditSubProc(_PROCESS_INFORMATION *hWnd, HWND Msg, WPARAM wParam, LPARAM lParam)
{
  if ( (_DWORD)Msg == 177 && !wParam && lParam == -2 )
    return 0;
  else
    return CallWindowProcA(g_lpfnOldMEditWndProc, (HWND)hWnd, (UINT)Msg, wParam, lParam);
}


__int64 __fastcall LicenseDlgProc(_PROCESS_INFORMATION *hWnd, int a2, __int64 a3)
{
  int v4; // edx
  int v5; // edx
  int v6; // edx
  INT_PTR v7; // rdx
  HWND DesktopWindow; // rax
  HWND DlgItem; // rbx

  v4 = a2 - 15;
  if ( v4 )
  {
    v5 = v4 - 1;
    if ( !v5 )
      goto LABEL_8;
    v6 = v5 - 256;
    if ( !v6 )
    {
      DesktopWindow = GetDesktopWindow();
      CenterWindow((HWND)hWnd, DesktopWindow);
      SetDlgItemTextA((HWND)hWnd, 2100, g_szLicense);
      SetWindowTextA((HWND)hWnd, Caption);
      SetForegroundWindow((HWND)hWnd);
      DlgItem = GetDlgItem((HWND)hWnd, 2100);
      g_lpfnOldMEditWndProc = (WNDPROC)GetWindowLongPtrA(DlgItem, -4);
      SetWindowLongPtrA(DlgItem, -4, (LONG_PTR)MEditSubProc);
      return 1;
    }
    if ( v6 == 1 )
    {
      if ( a3 == 6 )
      {
        v7 = 1;
LABEL_9:
        EndDialog((HWND)hWnd, v7);
        return 1;
      }
      if ( a3 != 7 )
        return 1;
LABEL_8:
      v7 = 0;
      goto LABEL_9;
    }
  }
  else if ( !dword_14000C840 )
  {
    SendDlgItemMessageA((HWND)hWnd, 2100, 0xB1u, 0xFFFFFFFFFFFFFFFFuLL, 0);
    dword_14000C840 = 1;
  }
  return 0;
}


__int64 __fastcall TempDirDlgProc(HWND hDlg, int a2, __int64 a3)
{
  int v4; // edx
  int v5; // edx
  __int64 v7; // r8
  __int64 v8; // r8
  int StringA; // eax
  HWND v10; // rcx
  INT_PTR v11; // rdx
  unsigned __int64 v12; // rax
  HWND DesktopWindow; // rax
  HWND DlgItem; // rax

  v4 = a2 - 16;
  if ( v4 )
  {
    v5 = v4 - 256;
    if ( !v5 )
    {
      DesktopWindow = GetDesktopWindow();
      CenterWindow(hDlg, DesktopWindow);
      SetWindowTextA(hDlg, Caption);
      SendDlgItemMessageA(hDlg, 2101, 0xC5u, 0x103u, 0);
      if ( g_wOSVer == 1 )
      {
        DlgItem = GetDlgItem(hDlg, 2102);
        EnableWindow(DlgItem, 0);
      }
      return 1;
    }
    if ( v5 != 1 )
      return 0;
    v7 = a3 - 1;
    if ( v7 )
    {
      v8 = v7 - 1;
      if ( v8 )
      {
        if ( v8 == 2100 )
        {
          StringA = LoadStringA(g_hInst, 0x3E8u, Buffer, 512);
          v10 = hDlg;
          if ( StringA )
          {
            if ( !(unsigned int)BrowseForDir(hDlg) || SetDlgItemTextA(hDlg, 2101, &pszDest) )
              return 1;
            v10 = hDlg;
          }
          MsgBox2Param(v10, 0x10u, 0);
          v11 = 0;
          goto LABEL_30;
        }
      }
      else
      {
        EndDialog(hDlg, 0);
        g_dwExitCode = -2147023673;
      }
      return 1;
    }
    if ( GetDlgItemTextA(hDlg, 2101, &PathName, 260) )
    {
      v12 = -1;
      do
        ++v12;
      while ( *(&PathName + v12) );
      if ( v12 >= 3 && (byte_14000D611 == 58 || PathName == 92 && byte_14000D611 == 92) )
      {
        if ( GetFileAttributesA(&PathName) != -1 )
          goto LABEL_25;
        if ( (unsigned int)MsgBox2Param(hDlg, 0x20u, 4) != 6 )
          return 1;
        if ( CreateDirectoryA(&PathName, 0) )
        {
LABEL_25:
          AddPath(&PathName, 0x104u, pszCabPath);
          if ( (unsigned int)IsGoodTempDir(&PathName) )
          {
            if ( (PathName != 92 || byte_14000D611 != 92) && !(unsigned int)IsEnoughSpace(&PathName) )
              return 1;
            v11 = 1;
LABEL_30:
            EndDialog(hDlg, v11);
            return 1;
          }
        }
      }
    }
    MsgBox2Param(hDlg, 0x10u, 0);
    return 1;
  }
  EndDialog(hDlg, 0);
  return 1;
}


__int64 __fastcall OverwriteDlgProc(HWND hWnd, int a2, unsigned __int64 a3)
{
  int v4; // edx
  int v5; // edx
  INT_PTR v7; // rdx
  HWND DesktopWindow; // rax

  v4 = a2 - 16;
  if ( !v4 )
  {
    v7 = 2;
    goto LABEL_12;
  }
  v5 = v4 - 256;
  if ( v5 )
  {
    if ( v5 != 1 )
      return 0;
    if ( a3 >= 6 )
    {
      if ( a3 <= 7 )
      {
LABEL_9:
        v7 = a3;
LABEL_12:
        EndDialog(hWnd, v7);
        return 1;
      }
      if ( a3 == 2105 )
      {
        dword_14000D600 = 1;
        goto LABEL_9;
      }
    }
  }
  else
  {
    DesktopWindow = GetDesktopWindow();
    CenterWindow(hWnd, DesktopWindow);
    SetWindowTextA(hWnd, Caption);
    SetDlgItemTextA(hWnd, 2104, lpString);
    SetForegroundWindow(hWnd);
  }
  return 1;
}


__int64 __fastcall ExtractDlgProc(HWND hWnd, int a2, __int64 a3)
{
  int v3; // esi
  HWND v4; // rdi
  int v5; // edx
  int v6; // edx
  int v7; // edx
  int v8; // edx
  INT_PTR v10; // rdx
  int v11; // eax
  HWND DesktopWindow; // rax
  HWND DlgItem; // rax
  HWND v14; // rax

  v3 = a3;
  v4 = hWnd;
  v5 = a2 - 16;
  if ( !v5 )
  {
LABEL_19:
    dword_14000D5FC = 1;
    goto LABEL_20;
  }
  v6 = v5 - 242;
  if ( !v6 )
  {
    if ( a3 != 27 )
      return 1;
    goto LABEL_19;
  }
  v7 = v6 - 14;
  if ( !v7 )
  {
    g_hwndExtractDlg = hWnd;
    DesktopWindow = GetDesktopWindow();
    CenterWindow(v4, DesktopWindow);
    if ( g_fOSSupportsFullUI )
    {
      DlgItem = GetDlgItem(v4, 2107);
      SendMessageA(DlgItem, 0x464u, 0, 3001);
      v14 = GetDlgItem(v4, 2107);
      SendMessageA(v14, 0x465u, 0xFFFFFFFFFFFFFFFFuLL, -65536);
    }
    SetWindowTextA(v4, Caption);
    hThread = CreateThread(0, 0, (LPTHREAD_START_ROUTINE)ExtractThread, 0, 0, &ThreadId);
    if ( hThread )
      return 1;
    MsgBox2Param(v4, 0x10u, 0);
LABEL_13:
    hWnd = v4;
LABEL_20:
    v10 = 0;
LABEL_21:
    EndDialog(hWnd, v10);
    return 1;
  }
  v8 = v7 - 1;
  if ( v8 )
  {
    if ( v8 != 3728 )
      return 0;
    TerminateThread(hThread, 0);
    v10 = v3;
    hWnd = v4;
    goto LABEL_21;
  }
  if ( a3 == 2 )
  {
    ResetEvent(g_hCancelEvent);
    v11 = MsgBox2Param(g_hwndExtractDlg, 0x20u, 4);
    if ( v11 != 6 && v11 != 1 )
    {
      SetEvent(g_hCancelEvent);
      return 1;
    }
    dword_14000D5FC = 1;
    SetEvent(g_hCancelEvent);
    WaitForObject(hThread);
    goto LABEL_13;
  }
  return 1;
}


DWORD __fastcall WaitForObject(void *a1)
{
  int v1; // ebx
  DWORD result; // eax
  struct tagMSG Msg; // [rsp+30h] [rbp-38h] BYREF
  PSID pHandles; // [rsp+70h] [rbp+8h] BYREF

  pHandles = a1;
  v1 = 0;
  while ( 1 )
  {
    result = MsgWaitForMultipleObjects(1u, &pHandles, 0, 0xFFFFFFFF, 0x4FFu);
    if ( !result )
      break;
    if ( PeekMessageA(&Msg, 0, 0, 0, 1u) )
    {
      do
      {
        if ( Msg.message == 18 )
          v1 = 1;
        else
          DispatchMessageA(&Msg);
        result = PeekMessageA(&Msg, 0, 0, 0, 1u);
      }
      while ( result );
      if ( v1 )
        break;
    }
  }
  return result;
}


__int64 __fastcall CheckOSVersion(__int64 a1)
{
  unsigned int v2; // ebx
  int v3; // edi
  __int16 v4; // ax
  int v5; // r10d
  int v6; // r11d
  __int64 v7; // r12
  int v8; // eax
  DWORD v9; // r8d
  int v10; // ecx
  bool v11; // cc
  const CHAR *v12; // r15
  int v13; // r14d
  int v14; // eax
  int v15; // eax
  int v16; // eax
  bool v17; // zf
  int v19[4]; // [rsp+38h] [rbp-D0h] BYREF
  _BYTE VersionInformation[160]; // [rsp+48h] [rbp-C0h] BYREF
  CHAR v21[272]; // [rsp+E8h] [rbp-20h] BYREF

  *(_DWORD *)VersionInformation = 148;
  v2 = 0;
  v3 = 0;
  if ( !GetVersionExA((LPOSVERSIONINFOA)VersionInformation) )
  {
    v3 = 1204;
LABEL_54:
    MsgBox2Param(0, 0x10u, 0);
    goto LABEL_69;
  }
  if ( *(_DWORD *)&VersionInformation[16] == 1 )
  {
    g_wOSVer = 0;
    g_fOSSupportsFullUI = 1;
    v4 = 0;
    g_fOSSupportsINFInstalls = 1;
  }
  else
  {
    if ( *(_DWORD *)&VersionInformation[16] != 2 )
    {
      v3 = 1226;
      goto LABEL_54;
    }
    g_wOSVer = 2;
    v4 = 2;
    g_fOSSupportsFullUI = 1;
    g_fOSSupportsINFInstalls = 1;
    if ( *(_DWORD *)&VersionInformation[4] > 3u )
    {
      if ( *(_DWORD *)&VersionInformation[4] >= 5u )
      {
        v4 = 3;
        g_wOSVer = 3;
      }
    }
    else
    {
      v4 = 1;
      g_wOSVer = 1;
      if ( *(_DWORD *)&VersionInformation[4] < 3u || *(_DWORD *)&VersionInformation[8] < 0x33u )
      {
        g_fOSSupportsFullUI = 0;
        g_fOSSupportsINFInstalls = 0;
      }
    }
  }
  if ( dword_14000CD14 || !a1 )
    goto LABEL_69;
  v19[0] = 0;
  v5 = 0;
  v6 = 0;
  v7 = (-(__int64)(v4 != 0) & 0xFFFFFFFFFFFFFFC4uLL) + a1 + 64;
  while ( 1 )
  {
    v8 = -1;
    v9 = 3 * v6;
    if ( *(_DWORD *)&VersionInformation[4] < *(_DWORD *)(v7 + 24LL * v6) )
    {
LABEL_17:
      v10 = -1;
      goto LABEL_22;
    }
    if ( *(_DWORD *)&VersionInformation[4] <= *(_DWORD *)(v7 + 24LL * v6) )
    {
      if ( *(_DWORD *)&VersionInformation[8] < *(_DWORD *)(v7 + 24LL * v6 + 4) )
        goto LABEL_17;
      v10 = *(_DWORD *)&VersionInformation[8] > *(_DWORD *)(v7 + 24LL * v6 + 4);
    }
    else
    {
      v10 = 1;
    }
LABEL_22:
    if ( *(_DWORD *)&VersionInformation[4] >= *(_DWORD *)(v7 + 24LL * v6 + 12) )
    {
      if ( *(_DWORD *)&VersionInformation[4] <= *(_DWORD *)(v7 + 24LL * v6 + 12) )
      {
        if ( *(_DWORD *)&VersionInformation[8] >= *(_DWORD *)(v7 + 24LL * v6 + 16) )
          v8 = *(_DWORD *)&VersionInformation[8] > *(_DWORD *)(v7 + 24LL * v6 + 16);
      }
      else
      {
        v8 = 1;
      }
    }
    if ( v10 >= 0 && v8 <= 0 )
    {
      if ( !v10 )
      {
        if ( v8 )
        {
          if ( (unsigned int)*(unsigned __int16 *)&VersionInformation[12] >= *(_DWORD *)(v7 + 24LL * v6 + 8) )
            goto LABEL_50;
        }
        else if ( (unsigned int)*(unsigned __int16 *)&VersionInformation[12] >= *(_DWORD *)(v7 + 24LL * v6 + 8) )
        {
          v11 = (unsigned int)*(unsigned __int16 *)&VersionInformation[12] <= *(_DWORD *)(v7 + 24LL * v6 + 20);
LABEL_37:
          if ( v11 )
            goto LABEL_50;
        }
        if ( v6 )
        {
          v3 = 1356;
          goto LABEL_40;
        }
        goto LABEL_46;
      }
      if ( v8 )
        goto LABEL_50;
      v11 = (unsigned int)*(unsigned __int16 *)&VersionInformation[12] <= *(_DWORD *)(v7 + 24LL * v6 + 20);
      goto LABEL_37;
    }
    if ( v6 == 1 )
      break;
LABEL_46:
    v5 = v6 + 1;
    v19[0] = v5;
    ++v6;
    if ( v5 >= 2 )
      goto LABEL_49;
  }
  v3 = 1356;
LABEL_49:
  if ( v3 )
    goto LABEL_53;
LABEL_50:
  if ( !*(_DWORD *)(a1 + 124) || (unsigned int)CheckFileVersion(a1, v21, v9, v19) )
    goto LABEL_69;
  v5 = v19[0];
  v3 = 1357;
LABEL_53:
  if ( (unsigned int)(v3 - 1356) > 1 )
    goto LABEL_54;
LABEL_40:
  v12 = 0;
  v13 = 0;
  if ( v3 == 1357 )
    v7 = *(unsigned int *)(a1 + 128) + 132LL + a1 + 60LL * v5;
  if ( v7 )
  {
    v12 = (const CHAR *)(*(unsigned int *)(v7 + 52) + a1 + 132);
    v14 = *(_DWORD *)(v7 + 48);
    if ( (v14 & 1) != 0 )
      v13 = 260;
    else
      v13 = (v14 & 2) != 0 ? 0x101 : 0;
  }
  if ( (word_14000CD18 & 1) == 0 && v12 && *v12 )
  {
    MessageBeep(0);
    if ( !(unsigned int)RunningOnWin95BiDiLoc()
      || (v17 = (unsigned int)IsBiDiLocalizedBinary() == 0, v15 = 1572912, v17) )
    {
      v15 = 48;
    }
    v16 = MessageBoxA(0, v12, Caption, v13 | v15);
    if ( (v13 & 4) != 0 )
    {
      v17 = v16 == 6;
    }
    else
    {
      if ( (v13 & 1) == 0 )
        goto LABEL_69;
      v17 = v16 == 1;
    }
    if ( v17 )
      v3 = 0;
  }
  else
  {
    MsgBox2Param(0, 0x30u, 0);
  }
LABEL_69:
  LOBYTE(v2) = v3 == 0;
  return v2;
}


__int64 DisplayLicense()
{
  unsigned int Resource; // ebx
  CHAR *v1; // rax
  __int64 v3; // rcx
  __int64 v4; // rbx

  Resource = GetResource("LICENSE", 0, 0);
  v1 = (CHAR *)LocalAlloc(0x40u, Resource + 1);
  g_szLicense = v1;
  if ( !v1 )
  {
    MsgBox2Param(0, 0x10u, 0);
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  if ( !(unsigned int)GetResource("LICENSE", v1, Resource) )
  {
    MsgBox2Param(0, 0x10u, 0);
    LocalFree((HLOCAL)g_szLicense);
    g_dwExitCode = -2147023084;
    return 0;
  }
  if ( lstrcmpA(g_szLicense, "<None>") )
  {
    v4 = MyDialogBox(v3, 2001, 0, LicenseDlgProc, 0, 0);
    LocalFree((HLOCAL)g_szLicense);
    if ( !v4 )
    {
      g_dwExitCode = -2147023673;
      return 0;
    }
  }
  else
  {
    LocalFree((HLOCAL)g_szLicense);
  }
  g_dwExitCode = 0;
  return 1;
}


__int64 RunInstallCommand()
{
  int v0; // r15d
  int v1; // r12d
  int v2; // r14d
  __int64 v3; // rsi
  __int64 v4; // rdx
  const CHAR *v5; // rcx
  CHAR *v6; // rcx
  CHAR v7; // al
  CHAR *v8; // rax
  int v9; // ebx
  HMODULE Library; // rax
  HMODULE v11; // rdi
  FARPROC ProcAddress; // rdx
  char *v13; // rbx
  int v14; // ecx
  __int64 cbData; // [rsp+38h] [rbp-D0h] BYREF
  char *hMem; // [rsp+40h] [rbp-C8h] BYREF
  __int64 Destination; // [rsp+48h] [rbp-C0h] BYREF
  _QWORD v19[5]; // [rsp+50h] [rbp-B8h] BYREF
  int v20; // [rsp+78h] [rbp-90h]
  int v21; // [rsp+7Ch] [rbp-8Ch]
  int v22; // [rsp+80h] [rbp-88h]
  struct _STARTUPINFOA v23; // [rsp+88h] [rbp-80h] BYREF
  CHAR String1[272]; // [rsp+F8h] [rbp-10h] BYREF
  char Buffer[272]; // [rsp+208h] [rbp+100h] BYREF
  BYTE Data[576]; // [rsp+318h] [rbp+210h] BYREF

  v0 = 0;
  v1 = 0;
  g_dwExitCode = 0;
  if ( !dword_14000CD08 && (unsigned int)GetResource("REBOOT", &dword_14000DE5C, 4u) - 1 > 3 )
  {
LABEL_24:
    MsgBox2Param(0, 0x10u, 0);
    g_dwExitCode = -2147023084;
    return 0;
  }
  v2 = 0;
  v3 = -1;
  while ( 1 )
  {
    LODWORD(cbData) = 0;
    memset_0(&v23.cb + 1, 0, 0x64u);
    v23.cb = 104;
    if ( byte_14000CF22 )
    {
      v4 = 260;
      v6 = String1;
      do
      {
        if ( v4 == -2147483386 )
          break;
        v7 = v6[&byte_14000CF22 - String1];
        if ( !v7 )
          break;
        *v6++ = v7;
        --v4;
      }
      while ( v4 );
      v8 = v6 - 1;
      if ( v4 )
        v8 = v6;
      *v8 = 0;
      goto LABEL_32;
    }
    if ( (unsigned int)GetResource("SHOWWINDOW", &Destination, 4u) - 1 > 3 )
      goto LABEL_24;
    switch ( (_DWORD)Destination )
    {
      case 1:
        v23.wShowWindow = 0;
        break;
      case 2:
        v23.wShowWindow = 6;
        break;
      case 3:
        v23.wShowWindow = 3;
        break;
      default:
        goto LABEL_13;
    }
    v23.dwFlags = 1;
LABEL_13:
    if ( v2 )
      goto LABEL_32;
    if ( word_14000CD18 )
    {
      if ( (word_14000CD18 & 1) != 0 )
      {
        v5 = "ADMQCMD";
      }
      else
      {
        if ( (word_14000CD18 & 2) == 0 )
          return 0;
        v5 = "USRQCMD";
      }
      if ( !(unsigned int)GetResource(v5, String1, 0x104u) )
        goto LABEL_24;
      if ( CompareStringA(0x7Fu, 1u, String1, -1, "<None>", -1) )
        v0 = 1;
    }
    if ( !v0 )
      break;
LABEL_36:
    if ( !(unsigned int)AnalyzeCmd(String1, v4, &hMem, &cbData) )
      return 0;
    v9 = cbData;
    if ( !v1 && g_wOSVer != 1 && g_CMD )
    {
      if ( (_DWORD)cbData )
        goto LABEL_43;
      v1 = 1;
      AddRegRunOnce();
    }
    if ( !v9 )
      goto LABEL_59;
LABEL_43:
    if ( !g_fOSSupportsINFInstalls )
    {
      MsgBox2Param(0, 0x10u, 0);
      LocalFree(hMem);
      g_dwExitCode = -2147023829;
      return 0;
    }
    if ( (dword_14000DE64 & 4) == 0 )
    {
LABEL_59:
      v13 = hMem;
      if ( !hMem || !(unsigned int)RunApps(hMem, &v23) )
        goto LABEL_64;
      goto LABEL_61;
    }
    Library = (HMODULE)MyLoadLibrary();
    v11 = Library;
    if ( !Library )
    {
      MsgBox2Param(0, 0x10u, 0);
      goto LABEL_67;
    }
    ProcAddress = GetProcAddress(Library, aDoinfinstall);
    if ( !ProcAddress )
    {
      MsgBox2Param(0, 0x10u, 0);
      FreeLibrary(v11);
LABEL_67:
      LocalFree(hMem);
      g_dwExitCode = MyGetLastError();
      return 0;
    }
    v13 = hMem;
    v19[1] = Caption;
    v19[3] = &PathName;
    LOWORD(v20) = g_wOSVer;
    v14 = (unsigned __int16)word_14000CD18;
    v19[4] = String1;
    v19[0] = 0;
    v19[2] = hMem;
    v21 = (unsigned __int16)word_14000CD18;
    if ( dword_14000CD10 )
    {
      v14 = (unsigned __int16)word_14000CD18 | 0x10000;
      v21 = v14;
    }
    if ( (dword_14000DE64 & 8) != 0 )
    {
      v14 |= 0x20000u;
      v21 = v14;
    }
    if ( (dword_14000DE64 & 0x10) != 0 )
    {
      v14 |= 0x40000u;
      v21 = v14;
    }
    if ( (dword_14000D028 & 0x40) != 0 )
    {
      v14 |= 0x80000u;
      v21 = v14;
    }
    if ( (dword_14000D028 & 0x80u) != 0 )
      v21 = v14 | 0x100000;
    v22 = dword_14000DE68;
    g_dwExitCode = ((__int64 (__fastcall *)(_QWORD *))ProcAddress)(v19);
    if ( g_dwExitCode < 0 )
    {
      FreeLibrary(v11);
LABEL_64:
      LocalFree(v13);
      return 0;
    }
    FreeLibrary(v11);
LABEL_61:
    LocalFree(v13);
    if ( (unsigned int)++v2 >= 2 )
      goto LABEL_70;
  }
  if ( !(unsigned int)GetResource("RUNPROGRAM", String1, 0x104u) )
    goto LABEL_24;
LABEL_32:
  if ( v2 != 1 )
    goto LABEL_36;
  if ( !(unsigned int)GetResource("POSTRUNPROGRAM", String1, 0x104u) )
    goto LABEL_24;
  if ( !byte_14000CF22 && CompareStringA(0x7Fu, 1u, String1, -1, "<None>", -1) != 2 )
    goto LABEL_36;
LABEL_70:
  if ( g_bConvertRunOnce && g_szRegValName[0] && !RegOpenKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0x2001Fu, (PHKEY)&hMem) )
  {
    LODWORD(cbData) = 568;
    if ( !RegQueryValueExA((HKEY)hMem, g_szRegValName, 0, 0, Data, (LPDWORD)&cbData) )
    {
      memset_0(Buffer, 0, 0x104u);
      if ( GetSystemDirectoryA(Buffer, 0x104u) )
        AddPath(Buffer, 0x104u, pszCabPath);
      StringCchPrintfA(
        (STRSAFE_LPSTR)Data,
        0x238u,
        "rundll32.exe %sadvpack.dll,DelNodeRunDLL32 \"%s\"",
        Buffer,
        &PathName);
      do
        ++v3;
      while ( Data[v3] );
      RegSetValueExA((HKEY)hMem, g_szRegValName, 0, 1u, Data, v3 + 1);
    }
    RegCloseKey((HKEY)hMem);
  }
  return 1;
}


__int64 __fastcall RunApps(LPSTR lpCommandLine, LPSTARTUPINFOA lpStartupInfo)
{
  unsigned int v2; // esi
  DWORD v3; // edi
  DWORD v4; // ecx
  int v5; // ebx
  DWORD LastError; // eax
  DWORD ExitCode; // [rsp+50h] [rbp-B0h] BYREF
  struct _PROCESS_INFORMATION ProcessInformation; // [rsp+58h] [rbp-A8h] BYREF
  CHAR Buffer[512]; // [rsp+70h] [rbp-90h] BYREF

  v2 = 1;
  memset(&ProcessInformation, 0, sizeof(ProcessInformation));
  if ( !CreateProcessA(0, lpCommandLine, 0, 0, 0, 0x20u, 0, 0, lpStartupInfo, &ProcessInformation) )
  {
    g_dwExitCode = MyGetLastError();
    LastError = GetLastError();
    FormatMessageA(0x1000u, 0, LastError, 0, Buffer, 0x200u, 0);
    MsgBox2Param(0, 0x10u, 0);
    return 0;
  }
  WaitForSingleObject(ProcessInformation.hProcess, 0xFFFFFFFF);
  GetExitCodeProcess(ProcessInformation.hProcess, &ExitCode);
  v3 = ExitCode;
  if ( !dword_14000CD08 )
  {
    v4 = dword_14000DE5C;
    if ( (dword_14000DE5C & 1) != 0 && (dword_14000DE5C & 2) == 0 )
    {
      if ( (ExitCode & 0xFF000000) == 0xAA000000 )
        v4 = ExitCode;
      dword_14000DE5C = v4;
    }
  }
  if ( (dword_14000DE64 & 0x800) != 0 )
    goto LABEL_9;
  if ( g_uInfRebootOn
    || (v5 = g_dwRebootCheck, v5 != NeedRebootInit())
    || (v3 & 0xFF000000) == 0xAA000000 && (v3 & 1) != 0 )
  {
    g_dwExitCode = 3010;
    goto LABEL_17;
  }
  if ( (dword_14000DE64 & 0x200) != 0 )
LABEL_9:
    g_dwExitCode = v3;
LABEL_17:
  CloseHandle(ProcessInformation.hThread);
  CloseHandle(ProcessInformation.hProcess);
  if ( (dword_14000DE64 & 0x400) != 0 && (ExitCode & 0x80000000) != 0 )
    return 0;
  return v2;
}


HLOCAL FinishMessage()
{
  unsigned int Resource; // edi
  CHAR *v1; // rax
  CHAR *v2; // rbx

  Resource = GetResource("FINISHMSG", 0, 0);
  v1 = (CHAR *)LocalAlloc(0x40u, 8LL * (Resource + 1));
  v2 = v1;
  if ( !v1 )
    return (HLOCAL)MsgBox2Param(0, 0x10u, 0);
  if ( (unsigned int)GetResource("FINISHMSG", v1, Resource) )
  {
    if ( lstrcmpA(v2, "<None>") )
      MsgBox2Param(0, 0x40u, 0);
  }
  else
  {
    MsgBox2Param(0, 0x10u, 0);
  }
  return LocalFree(v2);
}


__int64 __fastcall BrowseCallback(HWND a1, int a2, __int64 a3, LPARAM a4)
{
  if ( a2 == 1 )
    SendMessageA(a1, 0x466u, 1u, a4);
  return 0;
}


__int64 __fastcall BrowseForDir(HWND a1)
{
  HMODULE LibraryA; // rax
  unsigned int v3; // ebx
  HMODULE v4; // rdi
  FARPROC ProcAddress; // r12
  FARPROC v6; // r14
  FARPROC v7; // r15
  __int64 v8; // rdx
  LPSTR v9; // rax
  LPSTR v10; // rsi
  __int64 v11; // rax
  __int64 v12; // rsi
  _QWORD v14[4]; // [rsp+30h] [rbp-68h] BYREF
  int v15; // [rsp+50h] [rbp-48h]
  __int64 (__fastcall *v16)(HWND, int, __int64, LPARAM); // [rsp+58h] [rbp-40h]
  CHAR *v17; // [rsp+60h] [rbp-38h]

  LibraryA = LoadLibraryA(aShell32Dll);
  v3 = 0;
  v4 = LibraryA;
  if ( !LibraryA )
    goto LABEL_17;
  ProcAddress = GetProcAddress(LibraryA, aShbrowseforfol);
  if ( !ProcAddress || (v6 = GetProcAddress(v4, (LPCSTR)0xC3)) == 0 || (v7 = GetProcAddress(v4, aShgetpathfromi)) == 0 )
  {
    FreeLibrary(v4);
LABEL_17:
    MsgBox2Param(a1, 0x10u, 0);
    return 0;
  }
  if ( !g_szBrowsePath[0] )
  {
    GetTempPathA(0x104u, g_szBrowsePath);
    v8 = -1;
    do
      ++v8;
    while ( g_szBrowsePath[v8] );
    v9 = CharPrevA(g_szBrowsePath, &g_szBrowsePath[v8]);
    v10 = v9;
    if ( *v9 == 92 && *CharPrevA(g_szBrowsePath, v9) != 58 )
      *v10 = 0;
  }
  pszDest[0] = 0;
  v14[3] = Buffer;
  v14[0] = a1;
  v16 = BrowseCallback;
  v14[1] = 0;
  v14[2] = 0;
  v15 = 1;
  v17 = g_szBrowsePath;
  v11 = ((__int64 (__fastcall *)(_QWORD *))ProcAddress)(v14);
  v12 = v11;
  if ( v11 )
  {
    ((void (__fastcall *)(__int64, CHAR *))v7)(v11, g_szBrowsePath);
    if ( g_szBrowsePath[0] )
      StringCchCopyA(pszDest, 0x104u, g_szBrowsePath);
    ((void (__fastcall *)(__int64))v6)(v12);
  }
  FreeLibrary(v4);
  LOBYTE(v3) = pszDest[0] != 0;
  return v3;
}


BOOL __fastcall CenterWindow(HWND hWnd, HWND a2)
{
  int v4; // r15d
  int v5; // esi
  int v6; // edi
  int v7; // r14d
  HDC DC; // rbx
  int DeviceCaps; // r12d
  int v10; // r13d
  int v11; // r8d
  int v12; // r9d
  struct tagRECT v15; // [rsp+48h] [rbp-28h] BYREF
  tagRECT Rect; // [rsp+58h] [rbp-18h] BYREF

  GetWindowRect(hWnd, &Rect);
  v4 = Rect.right - Rect.left;
  v5 = Rect.bottom - Rect.top;
  GetWindowRect(a2, &v15);
  v6 = v15.right - v15.left;
  v7 = v15.bottom - v15.top;
  DC = GetDC(hWnd);
  DeviceCaps = GetDeviceCaps(DC, 8);
  v10 = GetDeviceCaps(DC, 10);
  ReleaseDC(hWnd, DC);
  v11 = v15.left + (v6 - v4) / 2;
  if ( v11 >= 0 )
  {
    if ( v11 + v4 > DeviceCaps )
      v11 = DeviceCaps - v4;
  }
  else
  {
    v11 = 0;
  }
  v12 = v15.top + (v7 - v5) / 2;
  if ( v12 >= 0 )
  {
    if ( v12 + v5 > v10 )
      v12 = v10 - v5;
  }
  else
  {
    v12 = 0;
  }
  return SetWindowPos(hWnd, 0, v11, v12, 0, 0, 5u);
}


__int64 __fastcall MsgBox2Param(HWND hWnd, UINT a2, __int64 a3, __int64 a4, UINT uType, int a6)
{
  __int64 result; // rax
  int v10; // eax
  UINT v11; // r9d
  unsigned int v12; // ebx
  __int64 v13; // rax
  __int64 v14; // rcx
  int v15; // eax
  __int64 v16; // rcx
  SIZE_T v17; // r15
  char *v18; // rax
  CHAR *v19; // rdi
  __int64 v20; // rcx
  SIZE_T v21; // r14
  char *v22; // rax
  SIZE_T v23; // rsi
  char *v24; // rax
  int v25; // eax
  int v26; // r9d
  CHAR Text[64]; // [rsp+30h] [rbp-D0h] BYREF
  CHAR Buffer[512]; // [rsp+70h] [rbp-90h] BYREF

  result = 1;
  strcpy(Text, "LoadString() Error.  Could not load string resource.");
  if ( (word_14000CD18 & 1) != 0 )
    return result;
  Buffer[0] = 0;
  LoadStringA(g_hInst, a2, Buffer, 512);
  if ( Buffer[0] )
  {
    v12 = -1;
    v13 = -1;
    if ( a4 )
    {
      do
        ++v13;
      while ( *(_BYTE *)(a4 + v13) );
      v14 = -1;
      do
        ++v14;
      while ( *(_BYTE *)(a3 + v14) );
      v15 = v14 + v13;
      v16 = -1;
      do
        ++v16;
      while ( Buffer[v16] );
      v17 = (unsigned int)(v16 + v15 + 100);
      v18 = (char *)LocalAlloc(0x40u, v17);
      v19 = v18;
      if ( v18 )
      {
        StringCchPrintfA(v18, (unsigned int)v17, Buffer, a3, a4);
        goto LABEL_23;
      }
      return v12;
    }
    do
      ++v13;
    while ( Buffer[v13] );
    if ( a3 )
    {
      v20 = -1;
      do
        ++v20;
      while ( *(_BYTE *)(a3 + v20) );
      v21 = (unsigned int)(v20 + v13 + 100);
      v22 = (char *)LocalAlloc(0x40u, v21);
      v19 = v22;
      if ( !v22 )
        return v12;
      StringCchPrintfA(v22, (unsigned int)v21, Buffer, a3);
    }
    else
    {
      v23 = (unsigned int)(v13 + 1);
      v24 = (char *)LocalAlloc(0x40u, v23);
      v19 = v24;
      if ( !v24 )
        return v12;
      StringCchCopyA(v24, (unsigned int)v23, Buffer);
    }
LABEL_23:
    MessageBeep(uType);
    if ( !(unsigned int)RunningOnWin95BiDiLoc() || (v25 = IsBiDiLocalizedBinary(), v26 = 1638400, !v25) )
      v26 = 0x10000;
    v12 = MessageBoxA(hWnd, v19, Caption, a6 | uType | v26);
    LocalFree(v19);
    return v12;
  }
  if ( !(unsigned int)RunningOnWin95BiDiLoc() || (v10 = IsBiDiLocalizedBinary(), v11 = 1638416, !v10) )
    v11 = 65552;
  MessageBoxA(hWnd, Text, Caption, v11);
  return -1;
}


__int64 __fastcall GetResource(LPCSTR lpName, void *Destination, rsize_t DestinationSize)
{
  DWORD v4; // ebp
  HRSRC ResourceA; // rax
  DWORD v7; // eax
  DWORD v8; // ebx
  HRSRC v9; // rax
  HGLOBAL Resource; // rax
  void *v11; // rax
  void *v12; // rdi

  v4 = DestinationSize;
  ResourceA = FindResourceA(0, lpName, (LPCSTR)0xA);
  v7 = SizeofResource(0, ResourceA);
  v8 = v7;
  if ( v7 > v4 || !Destination )
    return v8;
  if ( v7 )
  {
    v9 = FindResourceA(0, lpName, (LPCSTR)0xA);
    Resource = LoadResource(0, v9);
    v11 = LockResource(Resource);
    v12 = v11;
    if ( v11 )
    {
      memcpy_s(Destination, v4, v11, v8);
      FreeResource(v12);
      return v8;
    }
  }
  return 0;
}


__int64 __fastcall CatDirAndFile(STRSAFE_LPSTR pszDest, STRSAFE_LPCSTR pszSrc, STRSAFE_LPCSTR a3)
{
  __int64 v5; // rax
  __int64 v6; // rcx

  StringCchCopyA(pszDest, 0x104u, pszSrc);
  v5 = -1;
  v6 = -1;
  do
    ++v6;
  while ( pszDest[v6] );
  if ( pszDest[v6 - 1] != 92 )
  {
    do
      ++v5;
    while ( pszDest[v5] );
    if ( pszDest[v5 - 1] != 47 && StringCchCatA(pszDest, 0x104u, "\\") < 0 )
      return 0;
  }
  StringCchCatA(pszDest, 0x104u, a3);
  return 1;
}


__int64 __fastcall CheckOverwrite(LPCSTR lpFileName)
{
  DWORD FileAttributesA; // eax
  __int64 v3; // rcx
  unsigned int v4; // ebx
  __int64 v5; // rax
  __int64 v6; // rax

  FileAttributesA = GetFileAttributesA(lpFileName);
  if ( FileAttributesA != -1 && (FileAttributesA & 0x10) == 0 )
  {
    v4 = 0;
    if ( !dword_14000D600 && (word_14000CD18 & 1) == 0 )
    {
      lpString = lpFileName;
      v5 = MyDialogBox(v3, 2003, g_hwndExtractDlg, OverwriteDlgProc, 0, 6) - 6;
      if ( v5 )
      {
        v6 = v5 - 1;
        if ( !v6 )
          return v4;
        if ( v6 == 2098 )
          dword_14000D600 = 1;
      }
    }
    SetFileAttributesA(lpFileName, 0x80u);
    return 1;
  }
  return 1;
}


__int64 __fastcall AddFile(STRSAFE_LPCSTR pszSrc)
{
  _QWORD *v2; // rdi
  __int64 result; // rax
  __int64 v4; // rbx
  __int64 v5; // rdx
  char *v6; // rax

  v2 = LocalAlloc(0x40u, 0x10u);
  if ( !v2 )
  {
    MsgBox2Param(g_hwndExtractDlg, 0x4B5u, 0, 0, 0x10u, 0);
    return 0;
  }
  v4 = -1;
  v5 = -1;
  do
    ++v5;
  while ( pszSrc[v5] );
  v6 = (char *)LocalAlloc(0x40u, v5 + 1);
  *v2 = v6;
  if ( !v6 )
  {
    MsgBox2Param(g_hwndExtractDlg, 0x4B5u, 0, 0, 0x10u, 0);
    LocalFree(v2);
    return 0;
  }
  do
    ++v4;
  while ( pszSrc[v4] );
  StringCchCopyA(v6, v4 + 1, pszSrc);
  result = 1;
  v2[1] = hMem;
  hMem = v2;
  return result;
}


INT_PTR __fastcall openfunc(const CHAR *pszFile, __int16 oflag, int pmode)
{
  int v3; // r14d
  int *v6; // rax
  __int64 v8; // rdx
  __int64 v9; // rcx
  HGLOBAL v10; // rax
  __int64 FileA; // rcx
  DWORD v12; // ebp
  DWORD dwCreationDisposition; // ebx
  CHAR v14; // al
  LPSTR v15; // rdi
  int v16; // r15d
  __int64 v17; // rax

  v3 = 0;
  v6 = (int *)&g_FileTable;
  do
  {
    if ( *v6 == 1 )
      break;
    ++v3;
    v6 += 8;
  }
  while ( (__int64)v6 < (__int64)&g_uInfRebootOn );
  if ( v3 == 40 )
  {
    MsgBox2Param(g_hwndExtractDlg, 0x4BBu, 0, 0, 0x10u, 0);
    return -1;
  }
  if ( lstrcmpA(pszFile, pszCabinet) )
  {
    if ( (oflag & 8) != 0 )
    {
      FileA = -1;
      goto LABEL_36;
    }
    v12 = (oflag & 3) != 0 ? 0x40000000 : 0x80000000;
    if ( (oflag & 0x100) != 0 )
    {
      if ( (oflag & 0x400) != 0 )
        dwCreationDisposition = 1;
      else
        dwCreationDisposition = (oflag & 0x200) != 0 ? 2 : 4;
    }
    else
    {
      dwCreationDisposition = (oflag & 0x200) != 0 ? 5 : 3;
    }
    FileA = (__int64)CreateFileA(pszFile, v12, 0, 0, dwCreationDisposition, 0x80u, 0);
    if ( FileA != -1 || dwCreationDisposition == 3 )
      goto LABEL_36;
    if ( !*pszFile )
    {
LABEL_35:
      FileA = (__int64)CreateFileA(pszFile, v12, 0, 0, dwCreationDisposition, 0x80u, 0);
LABEL_36:
      v8 = v3;
      v17 = 32LL * v3;
      *(_QWORD *)((char *)&g_FileTable + v17 + 24) = FileA;
      if ( FileA == -1 )
        return -1;
      *(_DWORD *)((char *)&g_FileTable + v17) = 0;
      *(_DWORD *)((char *)&g_FileTable + v17 + 4) = 0;
      return v8;
    }
    v14 = pszFile[1];
    v15 = (LPSTR)(pszFile + 2);
    v16 = 0;
    if ( v14 == 58 && *v15 == 92 )
    {
      v15 = (LPSTR)(pszFile + 3);
    }
    else
    {
      if ( *pszFile != 92 || v14 != 92 )
      {
        v15 = (LPSTR)(pszFile + 1);
LABEL_34:
        while ( v14 )
        {
          if ( v14 == 92 && *(v15 - 1) != 58 )
          {
            if ( v16 )
            {
              --v16;
            }
            else
            {
              *v15 = 0;
              CreateDirectoryA(pszFile, 0);
              *v15 = 92;
            }
          }
          v15 = CharNextA(v15);
          v14 = *v15;
        }
        goto LABEL_35;
      }
      v16 = 2;
    }
    v14 = *v15;
    goto LABEL_34;
  }
  if ( (oflag & 0x10B) != 0 )
    return -1;
  v8 = v3;
  v9 = 32LL * v3;
  *(_DWORD *)((char *)&g_FileTable + v9) = 0;
  v10 = g_Sess;
  *(_DWORD *)((char *)&g_FileTable + v9 + 16) = 0;
  *(_QWORD *)((char *)&g_FileTable + v9 + 8) = v10;
  *(_DWORD *)((char *)&g_FileTable + v9 + 20) = dword_14000D568;
  *(_DWORD *)((char *)&g_FileTable + v9 + 4) = 1;
  return v8;
}


__int64 __fastcall readfunc(INT_PTR hf, void *pv, UINT cb)
{
  INT_PTR v3; // rdi
  int v4; // ecx
  unsigned int v5; // ebx
  BOOL v6; // eax
  DWORD v7; // ecx
  DWORD NumberOfBytesRead; // [rsp+50h] [rbp+18h] BYREF

  NumberOfBytesRead = cb;
  v3 = 32 * hf;
  v4 = *((_DWORD *)&g_FileTable + 8 * hf + 1);
  if ( v4 )
  {
    if ( v4 == 1 )
    {
      v5 = *(_DWORD *)((char *)&g_FileTable + v3 + 20) - *(_DWORD *)((char *)&g_FileTable + v3 + 16);
      if ( cb < v5 )
        v5 = cb;
      memcpy_0(
        pv,
        (const void *)(*(_QWORD *)((char *)&g_FileTable + v3 + 8) + *(int *)((char *)&g_FileTable + v3 + 16)),
        (int)v5);
      *(_DWORD *)((char *)&g_FileTable + v3 + 16) += v5;
    }
    else
    {
      return (unsigned int)-1;
    }
  }
  else
  {
    v6 = ReadFile(*(HANDLE *)((char *)&g_FileTable + v3 + 24), pv, cb, &NumberOfBytesRead, 0);
    v7 = NumberOfBytesRead;
    if ( !v6 )
      return DWORDLONG_MAX;
    return v7;
  }
  return v5;
}


__int64 __fastcall writefunc(INT_PTR hf, void *pv, UINT cb)
{
  DWORD v6; // ebx
  __int64 v7; // rdx
  DWORD NumberOfBytesWritten; // [rsp+50h] [rbp+18h] BYREF

  NumberOfBytesWritten = cb;
  WaitForObject(g_hCancelEvent);
  if ( dword_14000D5FC )
    return 0xFFFFFFFFLL;
  if ( WriteFile(qword_14000D058[4 * hf], pv, NumberOfBytesWritten, &NumberOfBytesWritten, 0) )
  {
    v6 = NumberOfBytesWritten;
    if ( NumberOfBytesWritten != -1 )
    {
      v7 = NumberOfBytesWritten + dword_14000D82C;
      dword_14000D82C += NumberOfBytesWritten;
      if ( g_fOSSupportsFullUI )
      {
        if ( g_hwndExtractDlg )
          SendDlgItemMessageA(
            g_hwndExtractDlg,
            2106,
            0x402u,
            100 * v7 / (unsigned __int64)(unsigned int)dword_14000D824,
            0);
      }
    }
  }
  else
  {
    return DWORDLONG_MAX;
  }
  return v6;
}


__int64 __fastcall closefunc(INT_PTR hf)
{
  INT_PTR v1; // rbx
  unsigned int v2; // ecx
  BOOL v3; // eax

  v1 = 32 * hf;
  if ( *((_DWORD *)&g_FileTable + 8 * hf + 1) == 1 )
  {
    v2 = 0;
    *(_DWORD *)((char *)&g_FileTable + v1) = 1;
    *(_QWORD *)((char *)&g_FileTable + v1 + 8) = 0;
    *(_QWORD *)((char *)&g_FileTable + v1 + 16) = 0;
  }
  else
  {
    v3 = CloseHandle(*(HANDLE *)((char *)&g_FileTable + v1 + 24));
    v2 = 0;
    if ( v3 )
      *(_DWORD *)((char *)&g_FileTable + v1) = 1;
    else
      return (unsigned int)-1;
  }
  return v2;
}


__int64 __fastcall seekfunc(INT_PTR hf, unsigned int dist, int seektype)
{
  INT_PTR v3; // rcx
  DWORD v4; // r9d
  int v5; // r8d
  int v6; // r8d

  v3 = 32 * hf;
  v4 = 1;
  if ( *(_DWORD *)((char *)&g_FileTable + v3 + 4) != 1 )
  {
    if ( seektype )
    {
      v6 = seektype - 1;
      if ( v6 )
      {
        if ( v6 != 1 )
          return 0xFFFFFFFFLL;
        v4 = 2;
      }
    }
    else
    {
      v4 = 0;
    }
    dist = SetFilePointer(*(HANDLE *)((char *)&g_FileTable + v3 + 24), dist, 0, v4);
    if ( dist == -1 )
      return (unsigned int)-1;
    return dist;
  }
  if ( seektype )
  {
    v5 = seektype - 1;
    if ( !v5 )
    {
      dist += *(_DWORD *)((char *)&g_FileTable + v3 + 16);
      goto LABEL_7;
    }
    if ( v5 == 1 )
    {
      dist += *(_DWORD *)((char *)&g_FileTable + v3 + 20);
      goto LABEL_7;
    }
    return 0xFFFFFFFFLL;
  }
LABEL_7:
  *(_DWORD *)((char *)&g_FileTable + v3 + 16) = dist;
  return dist;
}


HGLOBAL __fastcall allocfunc(ULONG cb)
{
  return GlobalAlloc(0, cb);
}


// attributes: thunk
HGLOBAL __stdcall freefunc(HGLOBAL hMem)
{
}__int64 __fastcall fdiNotifyExtract(_XSAVE_FORMAT *__return_ptr retstr, __int64 fdint, PFDINOTIFICATION pfdin)
{
  int v5; // ecx
  int v6; // ecx
  int v7; // ecx
  const char *v8; // r8
  __int64 v9; // rax
  __int64 v10; // rcx
  __int64 v11; // rdi
  DWORD v12; // edx
  const char *v13; // r8
  __int64 v14; // rax
  __int64 v15; // rcx
  INT_PTR v16; // rbx
  FILETIME CreationTime; // [rsp+28h] [rbp-E0h] BYREF
  struct _FILETIME FileTime; // [rsp+30h] [rbp-D8h] BYREF
  CHAR FileName[272]; // [rsp+38h] [rbp-D0h] BYREF

  if ( dword_14000D5FC )
  {
    if ( (_DWORD)retstr == 3 )
      closefunc(*(_QWORD *)(fdint + 40));
    return -1;
  }
  if ( !(_DWORD)retstr )
    return (int)UpdateCabinetInfo(fdint, fdint, pfdin);
  v5 = (_DWORD)retstr - 1;
  if ( !v5 )
    return 0;
  v6 = v5 - 1;
  if ( !v6 )
  {
    if ( g_hwndExtractDlg )
      SetDlgItemTextA(g_hwndExtractDlg, 2103, *(LPCSTR *)(fdint + 8));
    v13 = *(const char **)(fdint + 8);
    v14 = -1;
    do
      ++v14;
    while ( v13[v14] );
    v15 = -1;
    do
      ++v15;
    while ( *(&PathName + v15) );
    if ( (int)v15 + (int)v14 + 1 >= 260 || !(unsigned int)CatDirAndFile(FileName, &PathName, v13) )
      return -1;
    if ( (unsigned int)CheckOverwrite(FileName) )
    {
      v16 = openfunc(FileName, 33538, 384);
      if ( v16 == -1 || !(unsigned int)AddFile(FileName) )
        return -1;
      ++dword_14000D820;
      return v16;
    }
    return 0;
  }
  v7 = v6 - 1;
  if ( v7 )
  {
    if ( v7 == 1 )
      return -1;
    return 0;
  }
  v8 = *(const char **)(fdint + 8);
  v9 = -1;
  do
    ++v9;
  while ( v8[v9] );
  v10 = -1;
  do
    ++v10;
  while ( *(&PathName + v10) );
  if ( (int)v10 + (int)v9 + 1 >= 260 )
    return -1;
  if ( !(unsigned int)CatDirAndFile(FileName, &PathName, v8) )
    return -1;
  v11 = 32LL * *(_QWORD *)(fdint + 40);
  if ( *(_DWORD *)((char *)&g_FileTable + v11 + 4) == 1
    || !DosDateTimeToFileTime(*(_WORD *)(fdint + 48), *(_WORD *)(fdint + 50), &FileTime)
    || !LocalFileTimeToFileTime(&FileTime, &CreationTime)
    || !SetFileTime(*(HANDLE *)((char *)&g_FileTable + v11 + 24), &CreationTime, &CreationTime, &CreationTime) )
  {
    return -1;
  }
  closefunc(*(_QWORD *)(fdint + 40));
  v12 = *(_WORD *)(fdint + 52) ? *(_WORD *)(fdint + 52) & 0x27 : 128;
  if ( !SetFileAttributesA(FileName, v12) )
    return -1;
  return 1;
}


__int64 __fastcall UpdateCabinetInfo(__int64 a1)
{
  _OWORD *v2; // rax
  __int64 v3; // rcx
  _OWORD *v4; // rdx
  __int128 v5; // xmm1
  __int128 v6; // xmm0
  __int64 v7; // rdx
  _BYTE *v8; // rcx
  __int64 v9; // r8
  _BYTE *v10; // r9
  bool v11; // zf
  _BYTE *v12; // rax
  __int64 v13; // r8
  _BYTE *v14; // rcx
  _BYTE *v15; // r9
  _BYTE *v16; // rax
  _BYTE *v17; // rcx
  _BYTE *v18; // r8
  _BYTE *v19; // rax

  v2 = &unk_14000D83C;
  v3 = 6;
  v4 = &unk_14000DB4C;
  do
  {
    *v2 = *v4;
    v2[1] = v4[1];
    v2[2] = v4[2];
    v2[3] = v4[3];
    v2[4] = v4[4];
    v2[5] = v4[5];
    v2[6] = v4[6];
    v2 += 8;
    v5 = v4[7];
    v4 += 8;
    *(v2 - 1) = v5;
    --v3;
  }
  while ( v3 );
  v6 = *v4;
  v7 = 260;
  v8 = &unk_14000DB4C;
  v9 = 260;
  *v2 = v6;
  v10 = *(_BYTE **)(a1 + 24);
  do
  {
    if ( v9 == -2147483386 )
      break;
    if ( !*v10 )
      break;
    *v8++ = *v10++;
    --v9;
  }
  while ( v9 );
  v11 = v9 == 0;
  v12 = v8 - 1;
  v13 = 260;
  if ( !v11 )
    v12 = v8;
  v14 = &unk_14000DC50;
  *v12 = 0;
  v15 = *(_BYTE **)(a1 + 8);
  do
  {
    if ( v13 == -2147483386 )
      break;
    if ( !*v15 )
      break;
    *v14++ = *v15++;
    --v13;
  }
  while ( v13 );
  v16 = v14 - 1;
  if ( v13 )
    v16 = v14;
  v17 = &unk_14000DD54;
  *v16 = 0;
  v18 = *(_BYTE **)(a1 + 16);
  do
  {
    if ( v7 == -2147483386 )
      break;
    if ( !*v18 )
      break;
    *v17++ = *v18++;
    --v7;
  }
  while ( v7 );
  v19 = v17 - 1;
  if ( v7 )
    v19 = v17;
  *v19 = 0;
  word_14000DE58 = *(_WORD *)(a1 + 54);
  word_14000DE5A = *(_WORD *)(a1 + 56);
  return 0;
}


_BOOL8 VerifyCabinet()
{
  HFDI v0; // rdi
  INT_PTR v1; // rax
  INT_PTR v2; // rbx
  _BOOL8 result; // rax
  _BYTE pfdici[40]; // [rsp+50h] [rbp-38h] BYREF

  memset(pfdici, 0, 24);
  v0 = FDICreate(
         (PFNALLOC)allocfunc,
         (PFNFREE)freefunc,
         (PFNOPEN)openfunc,
         (PFNREAD)readfunc,
         (PFNWRITE)writefunc,
         (PFNCLOSE)closefunc,
         (PFNSEEK)seekfunc,
         1,
         (PERF)&pfdici[24]);
  result = 0;
  if ( v0 )
  {
    v1 = openfunc(pszCabinet, 0x8000, 384);
    v2 = v1;
    if ( v1 != -1
      && FDIIsCabinet(v0, v1, (PFDICABINETINFO)pfdici)
      && *(_DWORD *)pfdici == dword_14000D568
      && !*(_DWORD *)&pfdici[16]
      && !*(_DWORD *)&pfdici[20]
      && (unsigned int)closefunc(v2) != -1
      && FDIDestroy(v0) )
    {
      return 1;
    }
  }
  return result;
}


FILETIME __fastcall ExtractThread(LPSTR lpThreadParameter)
{
  HRSRC ResourceA; // rax
  HGLOBAL Resource; // rax
  FILETIME result; // rax
  HWND DlgItem; // rax
  HWND v5; // rax
  UINT v6; // edx
  HFDI v7; // rdi
  BOOL v8; // ebx

  dword_14000D568 = GetResource("CABINET", 0, 0);
  ResourceA = FindResourceA(0, "CABINET", (LPCSTR)0xA);
  Resource = LoadResource(0, ResourceA);
  result = (FILETIME)LockResource(Resource);
  g_Sess = (HGLOBAL)result;
  if ( !*(_QWORD *)&result )
    return result;
  if ( g_hwndExtractDlg )
  {
    DlgItem = GetDlgItem(g_hwndExtractDlg, 2114);
    ShowWindow(DlgItem, 0);
    v5 = GetDlgItem(g_hwndExtractDlg, 2113);
    ShowWindow(v5, 5);
  }
  if ( VerifyCabinet() )
  {
    v7 = FDICreate(
           (PFNALLOC)allocfunc,
           (PFNFREE)freefunc,
           (PFNOPEN)openfunc,
           (PFNREAD)readfunc,
           (PFNWRITE)writefunc,
           (PFNCLOSE)closefunc,
           (PFNSEEK)seekfunc,
           1,
           &perf);
    if ( v7 )
    {
      v8 = FDICopy(v7, pszCabinet, (LPSTR)pszCabPath, 0, (PFNFDINOTIFY)fdiNotifyExtract, 0, &g_Sess);
      if ( !v8 || FDIDestroy(v7) )
        goto LABEL_11;
    }
    v6 = perf.erfOper + 1300;
  }
  else
  {
    v6 = 1210;
  }
  MsgBox2Param(g_hwndExtractDlg, v6, 0, 0, 0x10u, 0);
  v8 = 0;
LABEL_11:
  if ( g_Sess )
  {
    FreeResource(g_Sess);
    g_Sess = 0;
  }
  if ( !v8 && !dword_14000D5FC )
    MsgBox2Param(0, 0x4F8u, 0, 0, 0x10u, 0);
  if ( (word_14000CD18 & 1) == 0 && (dword_14000DE64 & 1) == 0 )
    SendMessageA(g_hwndExtractDlg, 0xFA1u, v8, 0);
  return (FILETIME)v8;
}


__int64 GetFileList()
{
  UINT v0; // edx

  if ( (unsigned int)GetResource("FILESIZES", &g_dwFileSizes, 0x24u) != 36 )
  {
    v0 = 1201;
LABEL_3:
    MsgBox2Param(0, v0, 0, 0, 0x10u, 0);
    g_dwExitCode = -2147023084;
    return 0;
  }
  dword_14000D824 = dword_14000CCE0;
  if ( !dword_14000CCE0 )
  {
    v0 = 1222;
    goto LABEL_3;
  }
  GetResource("PACKINSTSPACE", &dword_14000DE68, 4u);
  if ( !(unsigned int)TravelUpdatedFiles(ProcessUpdatedFile_Size) )
  {
    MsgBox2Param(0, 0x4C6u, 0, 0, 0x10u, 0);
    return 0;
  }
  return 1;
}


__int64 GetUsersPermission()
{
  unsigned int Resource; // ebx
  HLOCAL v1; // rax
  void *v2; // rdi
  int v4; // ebx

  Resource = GetResource("UPROMPT", 0, 0);
  v1 = LocalAlloc(0x40u, Resource + 1);
  v2 = v1;
  if ( v1 )
  {
    if ( (unsigned int)GetResource("UPROMPT", v1, Resource) )
    {
      if ( lstrcmpA((LPCSTR)v2, "<None>") )
      {
        v4 = MsgBox2Param(0, 0x3E9u, (__int64)v2, 0, 0x20u, 4);
        LocalFree(v2);
        if ( v4 != 6 )
        {
          g_dwExitCode = -2147023673;
          return 0;
        }
        g_dwExitCode = 0;
      }
      else
      {
        LocalFree(v2);
      }
      return 1;
    }
    MsgBox2Param(0, 0x4B1u, 0, 0, 0x10u, 0);
    LocalFree(v2);
    g_dwExitCode = -2147023084;
  }
  else
  {
    MsgBox2Param(0, 0x4B5u, 0, 0, 0x10u, 0);
    g_dwExitCode = MyGetLastError();
  }
  return 0;
}


LSTATUS DeleteExtractedFiles()
{
  LPCSTR *v0; // rbx
  LPCSTR *v1; // rdi
  CHAR *v2; // rcx
  LSTATUS result; // eax
  __int64 v4; // rdx
  CHAR *v5; // rcx
  CHAR v6; // al
  CHAR *v7; // rax
  bool v8; // zf
  LPDWORD hKey; // [rsp+30h] [rbp-138h] BYREF
  CHAR v10[272]; // [rsp+40h] [rbp-128h] BYREF

  v0 = (LPCSTR *)hMem;
  while ( v0 )
  {
    v1 = v0;
    if ( !dword_14000CD04 && !dword_14000DE60 )
    {
      SetFileAttributesA(*v0, 0x80u);
      DeleteFileA(*v0);
    }
    v2 = (CHAR *)*v0;
    v0 = (LPCSTR *)v0[1];
    LocalFree(v2);
    LocalFree(v1);
  }
  result = g_CMD;
  if ( g_CMD && !dword_14000CD04 && !dword_14000DE60 )
  {
    v4 = 260;
    v5 = v10;
    do
    {
      if ( v4 == -2147483386 )
        break;
      v6 = v5[&PathName - v10];
      if ( !v6 )
        break;
      *v5++ = v6;
      --v4;
    }
    while ( v4 );
    v7 = v5 - 1;
    if ( v4 )
      v7 = v5;
    v8 = (dword_14000DE64 & 0x20) == 0;
    *v7 = 0;
    if ( !v8 )
      GetParentDir(v10);
    SetCurrentDirectoryA("..");
    DeleteMyDir(v10);
    result = g_CMD;
  }
  if ( g_wOSVer != 1 )
  {
    if ( result )
    {
      if ( g_szRegValName[0] )
      {
        result = RegOpenKeyExA(HKEY_LOCAL_MACHINE, SubKey, 0, 0x20006u, (PHKEY)&hKey);
        if ( !result )
        {
          RegDeleteValueA((HKEY)hKey, g_szRegValName);
          result = RegCloseKey((HKEY)hKey);
        }
      }
    }
  }
  g_CMD = 0;
  return result;
}


__int64 __fastcall GetNewTempDir(LPCSTR lpPathName, char *a2)
{
  unsigned int v2; // ebx
  int v4; // esi
  char pszDest[272]; // [rsp+20h] [rbp-138h] BYREF

  v2 = 0;
  v4 = 0;
  while ( 1 )
  {
    StringCchPrintfA(pszDest, 0x104u, "IXP%03d.TMP", v4++);
    StringCchCopyA(a2, 0x104u, lpPathName);
    AddPath(a2, 0x104u, pszDest);
    RemoveDirectoryA(a2);
    if ( GetFileAttributesA(a2) == -1 )
      break;
    if ( v4 >= 400 )
      goto LABEL_4;
  }
  if ( CreateDirectoryA(a2, 0) )
  {
    g_CMD = 1;
    return 1;
  }
LABEL_4:
  if ( GetTempFileNameA(lpPathName, "IXP", 0, a2) )
  {
    v2 = 1;
    DeleteFileA(a2);
    CreateDirectoryA(a2, 0);
  }
  return v2;
}


__int64 __fastcall CreateAndValidateSubdir(const CHAR *a1, int a2, int a3)
{
  __int64 v5; // rdx
  CHAR *v6; // rcx
  CHAR v7; // al
  CHAR *v8; // rax
  const char *v9; // r8
  __int64 v10; // rdi
  CHAR *v11; // rcx
  signed __int64 v12; // r9
  CHAR v13; // al
  CHAR *v14; // rax
  struct _SYSTEM_INFO SystemInfo; // [rsp+20h] [rbp-158h] BYREF
  char v17[272]; // [rsp+50h] [rbp-128h] BYREF

  if ( a2 )
  {
    if ( !(unsigned int)GetNewTempDir(a1, v17) )
      return 0;
    v5 = 260;
    v6 = &PathName;
    do
    {
      if ( v5 == -2147483386 )
        break;
      v7 = v6[v17 - &PathName];
      if ( !v7 )
        break;
      *v6++ = v7;
      --v5;
    }
    while ( v5 );
    v8 = v6 - 1;
    if ( v5 )
      v8 = v6;
    *v8 = 0;
    if ( (dword_14000DE64 & 0x20) == 0 )
      goto LABEL_19;
    GetSystemInfo(&SystemInfo);
    if ( SystemInfo.wProcessorArchitecture )
    {
      switch ( SystemInfo.wProcessorArchitecture )
      {
        case 1u:
          v9 = "mips";
          break;
        case 2u:
          v9 = "alpha";
          break;
        case 3u:
          v9 = "ppc";
          break;
        default:
LABEL_19:
          AddPath(&PathName, 0x104u, pszCabPath);
          goto LABEL_27;
      }
    }
    else
    {
      v9 = "i386";
    }
    AddPath(&PathName, 0x104u, v9);
    goto LABEL_19;
  }
  v10 = 260;
  v11 = &PathName;
  v12 = a1 - &PathName;
  do
  {
    if ( v10 == -2147483386 )
      break;
    v13 = v11[v12];
    if ( !v13 )
      break;
    *v11++ = v13;
    --v10;
  }
  while ( v10 );
  v14 = v11 - 1;
  if ( v10 )
    v14 = v11;
  *v14 = 0;
LABEL_27:
  if ( !(unsigned int)IsGoodTempDir(&PathName) )
  {
    if ( CreateDirectoryA(&PathName, 0) )
    {
      g_CMD = 1;
      goto LABEL_30;
    }
    g_dwExitCode = MyGetLastError();
    return 0;
  }
LABEL_30:
  if ( a3 && !(unsigned int)IsEnoughSpace(&PathName) )
  {
    if ( g_CMD )
    {
      g_CMD = 0;
      RemoveDirectoryA(&PathName);
    }
    return 0;
  }
  g_dwExitCode = 0;
  return 1;
}


__int64 GetTempDirectory()
{
  unsigned int Resource; // esi
  HLOCAL v1; // rax
  unsigned int v2; // ebx
  void *v3; // rdi
  int v5; // eax
  int v6; // ecx
  __int64 v7; // rcx
  int v8; // r8d
  __int64 v9; // rdx
  CHAR *v10; // rcx
  CHAR v11; // al
  CHAR *v12; // rax
  UINT DriveTypeA; // eax
  UINT v14; // edi
  CHAR v15; // cl
  char v16; // cl
  DWORD FileAttributesA; // eax
  DWORD DirectoryA; // eax
  __int64 v19; // rdx
  CHAR *v20; // rcx
  CHAR v21; // al
  CHAR *v22; // rax
  DWORD BytesPerSector; // [rsp+38h] [rbp-D0h] BYREF
  DWORD SectorsPerCluster; // [rsp+3Ch] [rbp-CCh] BYREF
  int TotalNumberOfClusters; // [rsp+40h] [rbp-C8h] BYREF
  DWORD NumberOfFreeClusters; // [rsp+44h] [rbp-C4h] BYREF
  CHAR RootPathName[272]; // [rsp+48h] [rbp-C0h] BYREF

  Resource = GetResource("RUNPROGRAM", 0, 0);
  v1 = LocalAlloc(0x40u, Resource + 1);
  v2 = 0;
  v3 = v1;
  if ( !v1 )
  {
    MsgBox2Param(0, 0x4B5u, 0, 0, 0x10u, 0);
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  if ( !(unsigned int)GetResource("RUNPROGRAM", v1, Resource) )
  {
    MsgBox2Param(0, 0x4B1u, 0, 0, 0x10u, 0);
    LocalFree(v3);
    g_dwExitCode = -2147023084;
    return 0;
  }
  v5 = lstrcmpA((LPCSTR)v3, "<None>");
  v6 = dword_14000DE60;
  if ( !v5 )
    v6 = 1;
  dword_14000DE60 = v6;
  LocalFree(v3);
  if ( Filename )
  {
    if ( Filename != 92 || (v8 = 0, byte_14000CE1F != 92) )
      v8 = 1;
    if ( !(unsigned int)CreateAndValidateSubdir(&Filename, 0, v8) )
    {
      MsgBox2Param(0, 0x4BEu, 0, 0, 0x10u, 0);
      return 0;
    }
    return 1;
  }
  if ( !dword_14000CD04 && !dword_14000DE60 )
  {
    if ( GetTempPathA(0x104u, &PathName)
      && ((unsigned int)CreateAndValidateSubdir(&PathName, 1, 3)
       || !(unsigned int)IsWindowsDrive(&PathName) && (unsigned int)CreateAndValidateSubdir(&PathName, 1, 1)) )
    {
      return 1;
    }
    while ( 1 )
    {
      v9 = 260;
      v10 = RootPathName;
      do
      {
        if ( v9 == -2147483386 )
          break;
        v11 = v10["A:\\" - RootPathName];
        if ( !v11 )
          break;
        *v10++ = v11;
        --v9;
      }
      while ( v9 );
      v12 = v10 - 1;
      if ( v9 )
        v12 = v10;
      *v12 = 0;
      if ( RootPathName[0] <= 90 )
        break;
LABEL_56:
      GetWindowsDirectoryA(RootPathName, 0x104u);
      if ( !(unsigned int)IsEnoughSpace(RootPathName) )
        return 0;
    }
    while ( 1 )
    {
      if ( (DriveTypeA = GetDriveTypeA(RootPathName), v14 = DriveTypeA, DriveTypeA != 6) && DriveTypeA != 3
        || GetFileAttributesA(RootPathName) == -1 )
      {
        if ( v14 != 2 )
          break;
        v15 = RootPathName[0];
        if ( (unsigned __int8)(RootPathName[0] - 65) <= 1u )
          goto LABEL_36;
        SectorsPerCluster = 0;
        BytesPerSector = 0;
        NumberOfFreeClusters = 0;
        TotalNumberOfClusters = 0;
        if ( !RootPathName[0] )
          goto LABEL_36;
        if ( !GetDiskFreeSpaceA(
                RootPathName,
                &SectorsPerCluster,
                &BytesPerSector,
                &NumberOfFreeClusters,
                (LPDWORD)&TotalNumberOfClusters)
          || (unsigned int)MulDiv(SectorsPerCluster * BytesPerSector, TotalNumberOfClusters, 1024) < 0x19000 )
        {
          break;
        }
      }
      if ( !(unsigned int)IsEnoughSpace(RootPathName)
        && ((unsigned int)IsWindowsDrive(RootPathName) || !(unsigned int)IsEnoughSpace(RootPathName)) )
      {
        break;
      }
      if ( (unsigned int)IsWindowsDrive(RootPathName) )
        GetWindowsDirectoryA(RootPathName, 0x104u);
      AddPath(RootPathName, 0x104u, "msdownld.tmp");
      FileAttributesA = GetFileAttributesA(RootPathName);
      if ( FileAttributesA == -1 )
        DirectoryA = CreateDirectoryA(RootPathName, 0);
      else
        DirectoryA = FileAttributesA & 0x10;
      if ( DirectoryA )
      {
        SetFileAttributesA(RootPathName, 2u);
        v19 = 260;
        v20 = &PathName;
        do
        {
          if ( v19 == -2147483386 )
            break;
          v21 = v20[RootPathName - &PathName];
          if ( !v21 )
            break;
          *v20++ = v21;
          --v19;
        }
        while ( v19 );
        v22 = v20 - 1;
        if ( v19 )
          v22 = v20;
        *v22 = 0;
        if ( (unsigned int)CreateAndValidateSubdir(&PathName, 1, 0) )
          return 1;
        v16 = RootPathName[0];
      }
      else
      {
        v16 = RootPathName[0] + 1;
        RootPathName[3] = 0;
        ++RootPathName[0];
      }
LABEL_55:
      if ( v16 > 90 )
        goto LABEL_56;
    }
    v15 = RootPathName[0];
LABEL_36:
    v16 = v15 + 1;
    RootPathName[0] = v16;
    goto LABEL_55;
  }
  LOBYTE(v2) = MyDialogBox(v7, 2002, 0, TempDirDlgProc, 0, 0) != 0;
  return v2;
}


__int64 __fastcall IsGoodTempDir(LPCSTR lpFileName)
{
  __int64 v2; // rbx
  unsigned int v3; // ebx
  char *v4; // rax
  char *v5; // rsi
  HANDLE FileA; // rbx
  DWORD FileAttributesA; // eax

  v2 = -1;
  do
    ++v2;
  while ( lpFileName[v2] );
  v3 = v2 + 20;
  v4 = (char *)LocalAlloc(0x40u, v3);
  v5 = v4;
  if ( !v4 )
  {
    MsgBox2Param(0, 0x4B5u, 0, 0, 0x10u, 0);
LABEL_5:
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  StringCchCopyA(v4, v3, lpFileName);
  AddPath(v5, v3, "TMP4351$.TMP");
  FileA = CreateFileA(v5, 0x40000000u, 0, 0, 1u, 0x4000080u, 0);
  LocalFree(v5);
  if ( FileA == (HANDLE)-1LL )
    goto LABEL_5;
  CloseHandle(FileA);
  FileAttributesA = GetFileAttributesA(lpFileName);
  if ( FileAttributesA == -1 || (FileAttributesA & 0x10) == 0 )
    goto LABEL_5;
  g_dwExitCode = 0;
  return 1;
}


__int64 __fastcall IsEnoughSpace(LPCSTR lpPathName, char a2, int a3)
{
  DWORD v6; // r14d
  unsigned int v7; // esi
  DWORD v8; // eax
  UINT v9; // edx
  __int64 v10; // rdx
  char *v11; // rcx
  __int64 v12; // rdi
  char v13; // al
  char *v14; // rax
  int v15; // ebx
  unsigned __int16 i; // ax
  unsigned int v17; // edx
  unsigned int v18; // r8d
  bool v19; // cc
  DWORD LastError; // eax
  DWORD BytesPerSector; // [rsp+48h] [rbp-C0h] BYREF
  DWORD SectorsPerCluster; // [rsp+4Ch] [rbp-BCh] BYREF
  DWORD NumberOfFreeClusters; // [rsp+50h] [rbp-B8h] BYREF
  DWORD TotalNumberOfClusters; // [rsp+54h] [rbp-B4h] BYREF
  DWORD FileSystemFlags; // [rsp+58h] [rbp-B0h] BYREF
  DWORD MaximumComponentLength; // [rsp+5Ch] [rbp-ACh] BYREF
  char v28; // [rsp+60h] [rbp-A8h] BYREF
  CHAR Buffer[272]; // [rsp+68h] [rbp-A0h] BYREF
  CHAR v30[512]; // [rsp+178h] [rbp+70h] BYREF

  GetCurrentDirectoryA(0x104u, Buffer);
  if ( !SetCurrentDirectoryA(lpPathName) )
  {
    MsgBox2Param(0, 0x4BCu, 0, 0, 0x10u, 0);
    g_dwExitCode = MyGetLastError();
    return 0;
  }
  SectorsPerCluster = 0;
  BytesPerSector = 0;
  NumberOfFreeClusters = 0;
  TotalNumberOfClusters = 0;
  if ( !GetDiskFreeSpaceA(0, &SectorsPerCluster, &BytesPerSector, &NumberOfFreeClusters, &TotalNumberOfClusters)
    || (v6 = SectorsPerCluster * BytesPerSector,
        (v7 = MulDiv(SectorsPerCluster * BytesPerSector, NumberOfFreeClusters, 1024)) == 0) )
  {
    memset_0(v30, 0, sizeof(v30));
    g_dwExitCode = MyGetLastError();
    LastError = GetLastError();
    FormatMessageA(0x1000u, 0, LastError, 0, v30, 0x200u, 0);
    v9 = 1200;
    goto LABEL_31;
  }
  if ( !GetVolumeInformationA(0, 0, 0, 0, &MaximumComponentLength, &FileSystemFlags, 0, 0) )
  {
    memset_0(v30, 0, sizeof(v30));
    g_dwExitCode = MyGetLastError();
    v8 = GetLastError();
    FormatMessageA(0x1000u, 0, v8, 0, v30, 0x200u, 0);
    v9 = 1273;
LABEL_31:
    MsgBox2Param(0, v9, (__int64)lpPathName, (__int64)v30, 0x10u, 0);
    SetCurrentDirectoryA(Buffer);
    return 0;
  }
  SetCurrentDirectoryA(Buffer);
  v10 = 6;
  v11 = &v28;
  v12 = lpPathName - &v28;
  do
  {
    if ( v10 == 4 )
      break;
    v13 = v11[v12];
    if ( !v13 )
      break;
    *v11++ = v13;
    --v10;
  }
  while ( v10 );
  v14 = v11 - 1;
  v15 = 512;
  if ( v10 )
    v14 = v11;
  *v14 = 0;
  for ( i = 0; i < 8u; ++i )
  {
    if ( v6 == v15 )
      break;
    v15 *= 2;
  }
  if ( i == 8 )
  {
    MsgBox2Param(0, 0x4C5u, 0, 0, 0x10u, 0);
    return 0;
  }
  if ( (dword_14000DE64 & 8) != 0 && (FileSystemFlags & 0x8000) != 0 )
  {
    v17 = 2 * g_dwFileSizes[i];
    v18 = dword_14000DE68 + ((unsigned int)dword_14000DE68 >> 2);
  }
  else
  {
    v18 = dword_14000DE68;
    v17 = g_dwFileSizes[i];
  }
  if ( (a2 & 3) == 3 )
  {
    v19 = v18 + v17 <= v7;
  }
  else if ( (a2 & 1) != 0 )
  {
    v19 = v17 <= v7;
  }
  else
  {
    v19 = v18 <= v7;
  }
  if ( !v19 )
    return DiskSpaceErrMsg(a3, v17, v18);
  g_dwExitCode = 0;
  return 1;
}


__int64 __fastcall RemoveLeadTailBlanks(char *a1, _DWORD *a2)
{
  char v2; // al
  int v3; // r8d
  char *v6; // r9
  char *v7; // r9
  __int64 result; // rax
  __int64 v9; // rcx
  int v10; // ecx
  __int64 i; // rdx
  char v12; // al

  v2 = *a1;
  v3 = 0;
  if ( *a1 )
  {
    v6 = a1;
    do
    {
      if ( v2 != 32 && (unsigned __int8)(v2 - 9) > 4u )
        break;
      ++v6;
      ++v3;
      v2 = *v6;
    }
    while ( *v6 );
  }
  v7 = &a1[v3];
  if ( !*v7 )
    return 0;
  v9 = -1;
  do
    ++v9;
  while ( v7[v9] );
  v10 = v9 - 1;
  for ( i = v10; i >= 0; --i )
  {
    v12 = v7[i];
    if ( v12 != 32 && (unsigned __int8)(v12 - 9) > 4u )
      break;
    --v10;
  }
  *a2 = v3;
  result = 1;
  a1[v3 + 1 + v10] = 0;
  return result;
}


__int64 __fastcall ParseCmdLine(CHAR *lpsz)
{
  LPSTR v1; // r14
  unsigned int v2; // esi
  unsigned __int64 v3; // rcx
  __int64 v4; // r8
  __int64 v5; // r9
  __int64 v6; // rdx
  __int64 v7; // rax
  unsigned __int8 v8; // al
  char v9; // al
  char *v10; // rbx
  unsigned __int8 v11; // al
  unsigned __int8 v12; // al
  char v13; // al
  char *v14; // rbx
  unsigned __int8 v15; // al
  unsigned int v16; // ebx
  char *v17; // rcx
  __int64 v18; // rax
  unsigned __int8 v19; // al
  __int64 v20; // r8
  char *v21; // r9
  CHAR *v22; // rdx
  char *v23; // rcx
  CHAR v24; // al
  char *v25; // rcx
  CHAR v26; // al
  CHAR *v27; // rax
  char *v28; // rbx
  unsigned __int64 v29; // rax
  char v30; // al
  unsigned int v32; // edi
  char *v33; // rbx
  __int64 v34; // rax
  __int64 v35; // r8
  char *v36; // rdx
  char *v37; // rcx
  char v38; // al
  char *v39; // rax
  _DWORD v40[4]; // [rsp+30h] [rbp-D0h] BYREF
  char v41; // [rsp+40h] [rbp-C0h] BYREF
  CHAR String2; // [rsp+41h] [rbp-BFh] BYREF
  char v43; // [rsp+42h] [rbp-BEh]
  char v44[269]; // [rsp+43h] [rbp-BDh] BYREF

  v1 = lpsz;
  v2 = 1;
  if ( !lpsz || !*lpsz )
    return 1;
  while ( 2 )
  {
    if ( !v2 )
      goto LABEL_29;
    while ( *v1 == 32 || (unsigned __int8)(*v1 - 9) <= 4u )
      v1 = CharNextA(v1);
    if ( !*v1 )
      goto LABEL_29;
    v3 = 0;
    v4 = 0;
    v5 = 0;
    v6 = 1;
    while ( (_DWORD)v4 )
    {
      if ( (_DWORD)v5 )
        goto LABEL_25;
LABEL_14:
      if ( *v1 == 34 )
      {
        if ( v1[1] == 34 )
        {
          if ( (unsigned int)v6 >= 0x104 )
            return 0;
          v6 = (unsigned int)(v6 + 1);
          *(&v41 + v3++) = 34;
          v7 = 2;
          goto LABEL_24;
        }
        if ( (_DWORD)v4 )
          v5 = 1;
        else
          v4 = 1;
      }
      else
      {
        if ( (unsigned int)v6 >= 0x104 )
          return 0;
        v6 = (unsigned int)(v6 + 1);
        *(&v41 + v3++) = *v1;
      }
      v7 = 1;
LABEL_24:
      v1 += v7;
      if ( !*v1 )
        goto LABEL_25;
    }
    if ( *v1 != 32 && (unsigned __int8)(*v1 - 9) > 4u )
      goto LABEL_14;
LABEL_25:
    if ( v3 >= 0x104 )
      _report_rangecheckfailure(v3, v6, v4, v5);
    *(&v41 + v3) = 0;
    if ( (_DWORD)v4 )
    {
      if ( !(_DWORD)v5 )
        goto LABEL_28;
LABEL_34:
      if ( ((v41 - 45) & 0xFD) == 0 )
      {
        v8 = (unsigned __int8)CharUpperA((LPSTR)String2);
        switch ( v8 )
        {
          case '?':
            MsgBox2Param(0, 0x521u, (__int64)pszCabPath, 0, 0x40u, 0);
            if ( g_hMutex )
              CloseHandle(g_hMutex);
            ExitProcess(0);
          case 'C':
            if ( !v43 )
            {
              dword_14000CD04 = 1;
              goto LABEL_43;
            }
            if ( v43 == 58 )
            {
              v32 = 4 - (v44[0] != 34);
              v33 = &v41 + v32;
              v34 = -1;
              do
                ++v34;
              while ( v33[v34] );
              if ( v34
                && (!ANSIStrChr(&v41 + 4 - (unsigned int)(v44[0] != 34)) || ANSIStrChr(v33))
                && (!ANSIStrChr(v33) || ANSIStrChr(v33)) )
              {
                v40[0] = v32;
                if ( (unsigned int)RemoveLeadTailBlanks(v33, v40) )
                {
                  v35 = 260;
                  v36 = &byte_14000CF22;
                  v37 = &v41 + (int)(v32 + v40[0]) - (_QWORD)&byte_14000CF22;
                  do
                  {
                    if ( v35 == -2147483386 )
                      break;
                    v38 = v36[(_QWORD)v37];
                    if ( !v38 )
                      break;
                    *v36++ = v38;
                    --v35;
                  }
                  while ( v35 );
                  v39 = v36 - 1;
                  if ( v35 )
                    v39 = v36;
                  *v39 = 0;
                  goto LABEL_43;
                }
              }
            }
            break;
          case 'D':
            goto LABEL_90;
          case 'N':
            if ( !v43 )
            {
              dword_14000CD0C = 1;
              goto LABEL_43;
            }
            if ( v43 == 58 )
            {
              v13 = v44[0];
              if ( v44[0] )
              {
                v14 = v44;
                do
                {
                  v15 = (unsigned __int8)CharUpperA((LPSTR)v13);
                  ++v14;
                  switch ( v15 )
                  {
                    case 'E':
                      dword_14000CD0C = 1;
                      break;
                    case 'G':
                      dword_14000CD10 = 1;
                      break;
                    case 'V':
                      dword_14000CD14 = 1;
                      break;
                    default:
                      v2 = 0;
                      break;
                  }
                  v13 = *v14;
                }
                while ( *v14 );
              }
              goto LABEL_43;
            }
            break;
          case 'Q':
            if ( !v43 )
              goto LABEL_69;
            if ( v43 == 58 )
            {
              v12 = (unsigned __int8)CharUpperA((LPSTR)v44[0]);
              switch ( v12 )
              {
                case '1':
                  goto LABEL_69;
                case 'A':
                  word_14000CD18 = 1;
                  goto LABEL_43;
                case 'U':
LABEL_69:
                  word_14000CD18 = 2;
                  goto LABEL_43;
              }
            }
            break;
          case 'R':
            if ( !v43 )
            {
              dword_14000DE5C = 3;
              dword_14000CD08 = 1;
              goto LABEL_43;
            }
            if ( v43 == 58 )
            {
              v9 = v44[0];
              dword_14000DE5C = 1;
              if ( !v44[0] )
                goto LABEL_43;
              v10 = v44;
              while ( 2 )
              {
                v11 = (unsigned __int8)CharUpperA((LPSTR)v9);
                ++v10;
                if ( v11 != 65 )
                {
                  switch ( v11 )
                  {
                    case 'D':
                      dword_14000D028 |= 0x40u;
                      break;
                    case 'I':
                      dword_14000DE5C &= ~2u;
                      goto LABEL_63;
                    case 'N':
                      dword_14000DE5C &= ~1u;
                      goto LABEL_63;
                    case 'P':
                      dword_14000D028 |= 0x80u;
                      break;
                    case 'S':
                      dword_14000DE5C |= 4u;
LABEL_63:
                      dword_14000CD08 = 1;
                      break;
                    default:
                      v2 = 0;
                      break;
                  }
                  v9 = *v10;
                  if ( !*v10 )
                    goto LABEL_43;
                  continue;
                }
                break;
              }
              dword_14000DE5C |= 2u;
              goto LABEL_63;
            }
            if ( CompareStringA(0x7Fu, 1u, "RegServer", -1, &String2, -1) == 2 )
              goto LABEL_43;
            break;
          case 'T':
LABEL_90:
            if ( v43 != 58 )
              break;
            v16 = 4 - (v44[0] != 34);
            v17 = &v41 + v16;
            v18 = -1;
            do
              ++v18;
            while ( v17[v18] );
            if ( !v18 )
              break;
            v40[0] = 4 - (v44[0] != 34);
            if ( !(unsigned int)RemoveLeadTailBlanks(v17, v40) )
              break;
            v19 = (unsigned __int8)CharUpperA((LPSTR)String2);
            v20 = 260;
            if ( v19 == 84 )
            {
              v21 = &Filename;
              v22 = &Filename;
              v23 = &v41 + (int)(v16 + v40[0]) - (_QWORD)&Filename;
              do
              {
                if ( v20 == -2147483386 )
                  break;
                v24 = v22[(_QWORD)v23];
                if ( !v24 )
                  break;
                *v22++ = v24;
                --v20;
              }
              while ( v20 );
            }
            else
            {
              v21 = byte_14000CD1A;
              v22 = byte_14000CD1A;
              v25 = &v41 + (int)(v16 + v40[0]) - (_QWORD)byte_14000CD1A;
              do
              {
                if ( v20 == -2147483386 )
                  break;
                v26 = v22[(_QWORD)v25];
                if ( !v26 )
                  break;
                *v22++ = v26;
                --v20;
              }
              while ( v20 );
            }
            v27 = v22 - 1;
            v28 = v21;
            if ( v20 )
              v27 = v22;
            *v27 = 0;
            AddPath(v21, 0x104u, pszCabPath);
            v29 = -1;
            do
              ++v29;
            while ( v28[v29] );
            if ( v29 < 3 )
              return 0;
            v30 = v28[1];
            if ( v30 != 58 && (*v28 != 92 || v30 != 92) )
              return 0;
LABEL_43:
            if ( !*v1 )
              goto LABEL_29;
            continue;
          default:
            break;
        }
        v2 = 0;
        goto LABEL_43;
      }
      return 0;
    }
    else
    {
      if ( !(_DWORD)v5 )
        goto LABEL_34;
LABEL_28:
      v2 = 0;
LABEL_29:
      if ( dword_14000CD0C && !Filename )
      {
        if ( GetModuleFileNameA(g_hInst, &Filename, 0x104u) )
          *(_BYTE *)(ANSIStrRChr(&Filename) + 1) = 0;
        else
          return 0;
      }
      return v2;
    }
  }
}


__int64 MyGetLastError()
{
  signed int LastError; // ecx
  __int64 result; // rax

  LastError = GetLastError();
  result = (unsigned __int16)LastError | 0x80070000;
  if ( LastError <= 0 )
    return (unsigned int)LastError;
  return result;
}


__int64 __fastcall TravelUpdatedFiles(unsigned int (__fastcall *a1)(_QWORD, _QWORD, char *, char *))
{
  int v1; // esi
  int v3; // r9d
  unsigned int v4; // edi
  HGLOBAL Resource; // rax
  unsigned int *v6; // rax
  unsigned int *v7; // rbx
  char *v8; // r8
  __int64 v9; // rax
  HRSRC ResourceA; // rax
  char pszDest[40]; // [rsp+30h] [rbp-28h] BYREF

  v1 = 0;
  v3 = 0;
  v4 = 1;
  while ( 1 )
  {
    StringCchPrintfA(pszDest, 0x14u, "UPDFILE%lu", v3);
    ResourceA = FindResourceA(0, pszDest, (LPCSTR)0xA);
    if ( !ResourceA )
      break;
    Resource = LoadResource(0, ResourceA);
    v6 = (unsigned int *)LockResource(Resource);
    v7 = v6;
    if ( !v6 )
    {
      g_dwExitCode = -2147023084;
      return 0;
    }
    v8 = (char *)(v6 + 2);
    v9 = -1;
    do
      ++v9;
    while ( v8[v9] );
    if ( !a1(*v7, v7[1], v8, &v8[v9 + 1]) )
    {
      v4 = 0;
      FreeResource(v7);
      return v4;
    }
    FreeResource(v7);
    v3 = ++v1;
  }
  return v4;
}


__int64 __fastcall ProcessUpdatedFile_Size(unsigned int a1)
{
  _DWORD *v2; // r10
  unsigned int v3; // r9d
  __int64 v4; // rbx
  int v5; // edx
  unsigned int v6; // ecx

  v2 = g_dwFileSizes;
  v3 = 512;
  v4 = 8;
  do
  {
    v5 = a1 % v3;
    v6 = a1 % v3 != 0 ? v3 : 0;
    v3 *= 2;
    *v2++ += a1 + v6 - v5;
    --v4;
  }
  while ( v4 );
  return 1;
}


__int64 __fastcall ProcessUpdatedFile_Write(DWORD nNumberOfBytesToWrite, __int64 a2, const char *a3, const void *a4)
{
  CHAR *v5; // rdx
  unsigned int v7; // ebx
  __int64 v8; // r9
  CHAR v9; // al
  CHAR *v10; // rax
  HANDLE FileA; // rax
  void *v12; // rdi
  DWORD NumberOfBytesWritten; // [rsp+40h] [rbp-148h] BYREF
  CHAR FileName[312]; // [rsp+50h] [rbp-138h] BYREF

  NumberOfBytesWritten = 0;
  v5 = FileName;
  v7 = 1;
  v8 = 260;
  do
  {
    if ( v8 == -2147483386 )
      break;
    v9 = v5[&PathName - FileName];
    if ( !v9 )
      break;
    *v5++ = v9;
    --v8;
  }
  while ( v8 );
  v10 = v5 - 1;
  if ( v8 )
    v10 = v5;
  *v10 = 0;
  AddPath(FileName, 0x104u, a3);
  FileA = CreateFileA(FileName, 0x40000000u, 0, 0, 2u, 0x80u, 0);
  v12 = FileA;
  if ( FileA == (HANDLE)-1LL )
  {
    g_dwExitCode = -2147024814;
    return 0;
  }
  else
  {
    if ( !WriteFile(FileA, a4, nNumberOfBytesToWrite, &NumberOfBytesWritten, 0)
      || nNumberOfBytesToWrite != NumberOfBytesWritten )
    {
      g_dwExitCode = -2147024814;
      v7 = 0;
    }
    CloseHandle(v12);
  }
  return v7;
}


HMODULE MyLoadLibrary()
{
  __int64 v0; // r8
  CHAR *v1; // rcx
  CHAR v2; // al
  CHAR *v3; // rax
  DWORD FileAttributesA; // eax
  CHAR FileName[296]; // [rsp+20h] [rbp-128h] BYREF

  v0 = 260;
  v1 = FileName;
  do
  {
    if ( v0 == -2147483386 )
      break;
    v2 = v1[&PathName - FileName];
    if ( !v2 )
      break;
    *v1++ = v2;
    --v0;
  }
  while ( v0 );
  v3 = v1 - 1;
  if ( v0 )
    v3 = v1;
  *v3 = 0;
  AddPath(FileName, 0x104u, "advpack.dll");
  FileAttributesA = GetFileAttributesA(FileName);
  if ( FileAttributesA == -1 || (FileAttributesA & 0x10) != 0 )
    return LoadLibraryA("advpack.dll");
  else
    return LoadLibraryExA(FileName, 0, 8u);
}


INT_PTR __fastcall MyDialogBox(
        __int64 a1,
        const CHAR *a2,
        HWND a3,
        INT_PTR (__stdcall *a4)(HWND, UINT, WPARAM, LPARAM),
        LPARAM dwInitParam,
        __int64 a6)
{
  HINSTANCE v6; // rbx
  HRSRC ResourceA; // rax
  DLGTEMPLATE *Resource; // rdi
  INT_PTR v11; // rax
  INT_PTR v12; // rbx

  v6 = g_hInst;
  ResourceA = FindResourceA(g_hInst, a2, (LPCSTR)5);
  if ( !ResourceA
    || (Resource = (DLGTEMPLATE *)LoadResource(v6, ResourceA)) == 0
    || (dwInitParam
      ? (v11 = DialogBoxIndirectParamA(v6, Resource, a3, a4, dwInitParam))
      : (v11 = DialogBoxIndirectParamA(v6, Resource, a3, a4, 0)),
        v12 = v11,
        FreeResource(Resource),
        v12 == -1) )
  {
    MsgBox2Param(0, 0x4FBu, 0, 0, 0x10u, 0);
    return a6;
  }
  return v12;
}


HRESULT __fastcall AddPath(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc)
{
  size_t v4; // rbp
  __int64 v5; // r8
  char *v8; // rbx

  v4 = (unsigned int)cchDest;
  v5 = -1;
  do
    ++v5;
  while ( pszDest[v5] );
  if ( (int)v5 + 1 >= (unsigned int)cchDest )
    return -2147024774;
  v8 = &pszDest[(unsigned int)v5];
  if ( v8 > pszDest && *CharPrevA(pszDest, &pszDest[(unsigned int)v5]) != 92 )
    *v8++ = 92;
  *v8 = 0;
  while ( *pszSrc == 32 )
    ++pszSrc;
  return StringCchCatA(pszDest, v4, pszSrc);
}


__int64 __fastcall GetParentDir(LPCSTR lpszStart)
{
  unsigned int v1; // esi
  __int64 v3; // rdx
  const CHAR *i; // rdx
  LPSTR v5; // rax
  const CHAR *v6; // rbx

  v1 = 0;
  v3 = -1;
  do
    ++v3;
  while ( lpszStart[v3] );
  for ( i = CharPrevA(lpszStart, &lpszStart[v3]); ; i = v5 )
  {
    v5 = CharPrevA(lpszStart, i);
    v6 = v5;
    if ( v5 <= lpszStart )
      break;
    if ( *v5 == 92 )
      goto LABEL_8;
  }
  if ( *v5 != 92 )
    return v1;
LABEL_8:
  if ( v5 == lpszStart || *CharPrevA(lpszStart, v5) == 58 )
    v6 = CharNextA(v6);
  *v6 = 0;
  return 1;
}


LPSTR __fastcall ANSIStrChr(CHAR *lpsz, __int16 a2)
{
  bool v2; // zf
  LPSTR v4; // rbx
  __int16 v5; // di
  BOOL v6; // eax

  v2 = *lpsz == 0;
  v4 = lpsz;
  while ( !v2 )
  {
    v5 = *(_WORD *)v4;
    if ( (unsigned __int8)*(_WORD *)v4 == (_BYTE)a2 )
    {
      if ( !IsDBCSLeadByte(*(_WORD *)v4) )
        return v4;
      v6 = v5 != a2;
    }
    else
    {
      v6 = 1;
    }
    if ( !v6 )
      return v4;
    v4 = CharNextA(v4);
    v2 = *v4 == 0;
  }
  return 0;
}


const CHAR *__fastcall ANSIStrRChr(LPCSTR lpsz, __int16 a2)
{
  const CHAR *v2; // rbx
  const CHAR *i; // rdi
  __int16 v5; // si
  BOOL v6; // eax
  const CHAR *v7; // rcx

  v2 = 0;
  for ( i = lpsz; *i; i = CharNextA(i) )
  {
    v5 = *(_WORD *)i;
    if ( (unsigned __int8)*(_WORD *)i == (_BYTE)a2 )
      v6 = IsDBCSLeadByte(*(_WORD *)i) && v5 != a2;
    else
      v6 = 1;
    v7 = i;
    if ( v6 )
      v7 = v2;
    v2 = v7;
  }
  return v2;
}


__int64 __fastcall EnumResLangProc(
        XMM_SAVE_AREA32 *__return_ptr retstr,
        HMODULE hModule,
        CHAR lpType,
        __int16 lpName,
        _STARTUPINFOW *wLanguage)
{
  __int64 result; // rax

  result = 1;
  if ( hModule == (HMODULE)wLanguage->lpReserved && LOWORD(wLanguage->cb) == (lpName & 0x3FF) )
  {
    *(&wLanguage->cb + 1) = 1;
    result = 0;
    LOWORD(wLanguage->cb) = lpName;
  }
  return result;
}


__int64 IsBiDiLocalizedBinary()
{
  unsigned int v0; // ebx
  HMODULE v1; // rdi
  _WORD lParam[2]; // [rsp+30h] [rbp-18h] BYREF
  int v4; // [rsp+34h] [rbp-14h]
  __int64 v5; // [rsp+38h] [rbp-10h]

  v0 = dword_14000C208;
  v1 = g_hInst;
  if ( dword_14000C208 == -2 )
  {
    v4 = 0;
    dword_14000C208 = 0;
    v0 = 1;
    lParam[0] = 1;
    v5 = 16;
    EnumResourceLanguagesA(g_hInst, (LPCSTR)0x10, (LPCSTR)1, (ENUMRESLANGPROCA)EnumResLangProc, (LONG_PTR)lParam);
    if ( v4
      || (v4 = 0,
          lParam[0] = 13,
          v5 = 16,
          EnumResourceLanguagesA(v1, (LPCSTR)0x10, (LPCSTR)1, (ENUMRESLANGPROCA)EnumResLangProc, (LONG_PTR)lParam),
          v4) )
    {
      dword_14000C208 = 1;
    }
    else
    {
      return (unsigned int)dword_14000C208;
    }
  }
  return v0;
}


__int64 RunningOnWin95BiDiLoc()
{
  unsigned int v0; // esi
  int v1; // edi
  LSTATUS Value; // ebx
  const CHAR *i; // rcx
  CHAR v4; // dl
  int v5; // edi
  DWORD cbData[2]; // [rsp+38h] [rbp-D0h] BYREF
  HKEY hKey; // [rsp+40h] [rbp-C8h] BYREF
  DWORD Type[4]; // [rsp+48h] [rbp-C0h] BYREF
  _OSVERSIONINFOA VersionInformation; // [rsp+58h] [rbp-B0h] BYREF
  BYTE Data[16]; // [rsp+F8h] [rbp-10h] BYREF

  v0 = dword_14000C20C;
  cbData[0] = 12;
  if ( dword_14000C20C == -2 )
  {
    v1 = 0;
    VersionInformation.dwOSVersionInfoSize = 148;
    dword_14000C20C = 0;
    if ( !GetVersionExA(&VersionInformation) )
      return (unsigned int)dword_14000C20C;
    v0 = 1;
    if ( VersionInformation.dwPlatformId != 1 )
      return (unsigned int)dword_14000C20C;
    if ( VersionInformation.dwMajorVersion != 4 )
      return (unsigned int)dword_14000C20C;
    if ( VersionInformation.dwMinorVersion >= 0xA )
      return (unsigned int)dword_14000C20C;
    if ( !GetSystemMetrics(74) )
      return (unsigned int)dword_14000C20C;
    if ( RegOpenKeyExA(HKEY_CURRENT_USER, "Control Panel\\Desktop\\ResourceLocale", 0, 0x20019u, &hKey) )
      return (unsigned int)dword_14000C20C;
    Value = RegQueryValueExA(hKey, pszCabPath, 0, Type, Data, cbData);
    RegCloseKey(hKey);
    if ( Value )
      return (unsigned int)dword_14000C20C;
    for ( i = (const CHAR *)Data; ; i = CharNextA(i) )
    {
      if ( (unsigned __int8)(*i - 48) > 9u )
      {
        v4 = *i - 32;
        if ( *i < 97 )
          v4 = *i;
        if ( (unsigned int)(v4 - 65) > 5 )
        {
          if ( i != (const CHAR *)Data )
          {
            v5 = v1 & 0x3FF;
            if ( v5 == 1 || v5 == 13 )
            {
              dword_14000C20C = 1;
              return v0;
            }
          }
          return (unsigned int)dword_14000C20C;
        }
        v1 = v4 + 16 * v1 - 55;
      }
      else
      {
        v1 = *i + 16 * (v1 - 3);
      }
    }
  }
  return v0;
}


// write access to const memory has been detected, the output may be wrong!
__int64 pre_c_init()
{
}__int64 pre_cpp_init()
{
  __int64 result; // rax

  dword_14000C244 = newmode;
  result = __getmainargs(&unk_14000C228, &unk_14000C230, &unk_14000C238, (unsigned int)dowildcard, &dword_14000C244);
  dword_14000C22C = result;
  return result;
}


__int64 WinMainCRTStartup()
{
  _security_init_cookie();
  return _mainCRTStartup();
}


int _mainCRTStartup()
{
  PVOID StackBase; // rbx
  int v1; // edi
  signed __int64 v2; // rax
  int v3; // eax
  _QWORD *i; // rbx
  int result; // eax
  char *v6; // rbx
  BOOL v7; // edi
  unsigned int v8; // ecx
  int wShowWindow; // r9d
  _STARTUPINFOW StartupInfo; // [rsp+40h] [rbp-78h] BYREF

  GetStartupInfoW(&StartupInfo);
  StackBase = NtCurrentTeb()->NtTib.StackBase;
  v1 = 0;
  while ( 1 )
  {
    v2 = _InterlockedCompareExchange64(&_native_startup_lock, (signed __int64)StackBase, 0);
    if ( !v2 )
      break;
    if ( (PVOID)v2 == StackBase )
    {
      v1 = 1;
      break;
    }
    Sleep(0x3E8u);
  }
  if ( _native_startup_state == 1 )
  {
    amsg_exit_0(31);
LABEL_18:
    if ( _native_startup_state == 1 )
    {
      initterm_0((_PVFV *)&_xc_a, (_PVFV *)&_xc_z);
      _native_startup_state = 2;
    }
    if ( !v1 )
      _InterlockedExchange64(&_native_startup_lock, 0);
    if ( _dyn_tls_init_callback && (unsigned int)IsNonwritableInCurrentImage(0x14000CB88LL) )
      _guard_dispatch_icall_fptr();
    v6 = _acmdln;
    v7 = 0;
    while ( 1 )
    {
      v8 = (unsigned __int8)*v6;
      if ( (unsigned __int8)v8 <= 0x20u && (!(_BYTE)v8 || !v7) )
        break;
      if ( (_BYTE)v8 == 34 )
        v7 = !v7;
      if ( _ismbblead(v8) )
        ++v6;
      ++v6;
    }
    while ( (unsigned __int8)(v8 - 1) <= 0x1Fu )
      LOBYTE(v8) = *++v6;
    wShowWindow = 10;
    if ( (StartupInfo.dwFlags & 1) != 0 )
      wShowWindow = StartupInfo.wShowWindow;
    result = WinMain((HINSTANCE)0x140000000LL, 0, v6, wShowWindow);
    dword_14000C220 = result;
    if ( !dword_14000C240 )
      exit(result);
    if ( !dword_14000C224 )
    {
      _cexit();
      return dword_14000C220;
    }
    return result;
  }
  v3 = _native_startup_state;
  if ( _native_startup_state )
  {
    dword_14000C224 = 1;
    goto LABEL_18;
  }
  _native_startup_state = 1;
  for ( i = &_xi_a; i < &_xi_z; ++i )
  {
    if ( v3 )
      return 255;
    if ( *i )
      v3 = _guard_dispatch_icall_fptr();
  }
  if ( !v3 )
    goto LABEL_18;
  return 255;
}


void __cdecl _security_check_cookie(uintptr_t StackCookie)
{
  __int64 v1; // rcx

  if ( StackCookie != _security_cookie )
LABEL_4:
    _report_gsfailure(StackCookie);
  v1 = __ROL8__(StackCookie, 16);
  if ( (_WORD)v1 )
  {
    StackCookie = __ROR8__(v1, 16);
    goto LABEL_4;
  }
}


BOOL __fastcall _raise_securityfailure(struct _EXCEPTION_POINTERS *ExceptionInfo)
{
  HANDLE CurrentProcess; // rax

  SetUnhandledExceptionFilter(0);
  UnhandledExceptionFilter(ExceptionInfo);
  CurrentProcess = GetCurrentProcess();
  return TerminateProcess(CurrentProcess, 0xC0000409);
}


void __cdecl  _report_gsfailure(uintptr_t StackCookie)
{
  struct _IMAGE_RUNTIME_FUNCTION_ENTRY *FunctionEntry; // [rsp+40h] [rbp-48h]
  DWORD64 ControlPc; // [rsp+48h] [rbp-40h]
  unsigned __int64 ImageBase; // [rsp+50h] [rbp-38h] BYREF
  unsigned __int64 EstablisherFrame; // [rsp+58h] [rbp-30h] BYREF
  PVOID HandlerData[5]; // [rsp+60h] [rbp-28h] BYREF

  RtlCaptureContext(&ContextRecord);
  ControlPc = ContextRecord.Rip;
  FunctionEntry = RtlLookupFunctionEntry(ContextRecord.Rip, &ImageBase, 0);
  if ( FunctionEntry )
  {
    RtlVirtualUnwind(0, ImageBase, ControlPc, FunctionEntry, &ContextRecord, HandlerData, &EstablisherFrame, 0);
  }
  else
  {
    ContextRecord.Rip = *(_QWORD *)ContextRecord.Rsp;
    ContextRecord.Rsp += 8LL;
  }
  qword_14000C260 = ContextRecord.Rip;
  ContextRecord.Rcx = StackCookie;
  dword_14000C250 = -1073740791;
  dword_14000C254 = 1;
  dword_14000C268 = 3;
  unk_14000C270 = 2;
  unk_14000C278 = _security_cookie;
  unk_14000C280 = _security_cookie_complement;
  HandlerData[2] = (PVOID)_security_cookie_complement;
  _raise_securityfailure((struct _EXCEPTION_POINTERS *)&off_140009000);
}


void  _report_rangecheckfailure()
{
  struct _IMAGE_RUNTIME_FUNCTION_ENTRY *FunctionEntry; // [rsp+40h] [rbp-38h]
  DWORD64 ControlPc; // [rsp+48h] [rbp-30h]
  unsigned __int64 ImageBase; // [rsp+50h] [rbp-28h] BYREF
  unsigned __int64 EstablisherFrame; // [rsp+58h] [rbp-20h] BYREF
  PVOID HandlerData; // [rsp+60h] [rbp-18h] BYREF

  RtlCaptureContext(&ContextRecord);
  ControlPc = ContextRecord.Rip;
  FunctionEntry = RtlLookupFunctionEntry(ContextRecord.Rip, &ImageBase, 0);
  if ( FunctionEntry )
  {
    RtlVirtualUnwind(0, ImageBase, ControlPc, FunctionEntry, &ContextRecord, &HandlerData, &EstablisherFrame, 0);
  }
  else
  {
    ContextRecord.Rip = *(_QWORD *)ContextRecord.Rsp;
    ContextRecord.Rsp += 8LL;
  }
  qword_14000C260 = ContextRecord.Rip;
  dword_14000C250 = -1073740791;
  dword_14000C254 = 1;
  dword_14000C268 = 1;
  unk_14000C270 = 8;
  _raise_securityfailure((struct _EXCEPTION_POINTERS *)&off_140009000);
}


__int64 __fastcall __CxxUnhandledExceptionFilter(struct _EXCEPTION_POINTERS *ExceptionInfo)
{
  PEXCEPTION_RECORD ExceptionRecord; // rax
  int v2; // ecx

  ExceptionRecord = ExceptionInfo->ExceptionRecord;
  if ( ExceptionInfo->ExceptionRecord->ExceptionCode == -529697949 && ExceptionRecord->NumberParameters == 4 )
  {
    v2 = ExceptionRecord->ExceptionInformation[0];
    if ( (unsigned int)(v2 - 429065504) <= 2 || v2 == 26820608 )
      terminate();
  }
  return 0;
}


__int64 _CxxSetUnhandledExceptionFilter()
{
  SetUnhandledExceptionFilter((LPTOP_LEVEL_EXCEPTION_FILTER)__CxxUnhandledExceptionFilter);
  return 0;
}


// attributes: thunk
__int64 XcptFilter_0()
{
}_DWORD *__fastcall RtlpImageNtHeader(__int64 a1)
{
  __int64 v1; // rdx
  _DWORD *v2; // rax

  v1 = 0;
  if ( (unsigned __int64)(a1 - 1) <= 0xFFFFFFFFFFFFFFFDuLL
    && *(_WORD *)a1 == 23117
    && *(_DWORD *)(a1 + 60) < 0x10000000u )
  {
    v2 = (_DWORD *)(a1 + *(int *)(a1 + 60));
    if ( *v2 != 17744 )
      return 0;
    return v2;
  }
  return (_DWORD *)v1;
}


__int64 __fastcall get_image_app_type(unsigned int a1)
{
  HMODULE ModuleHandleW; // rax
  _DWORD *v3; // rax
  __int64 result; // rax
  bool v5; // zf

  ModuleHandleW = GetModuleHandleW(0);
  if ( !ModuleHandleW )
    return a1;
  v3 = RtlpImageNtHeader((__int64)ModuleHandleW);
  if ( !v3 )
    return a1;
  if ( *((_WORD *)v3 + 46) == 2 )
    return 2;
  v5 = *((_WORD *)v3 + 46) == 3;
  result = 1;
  if ( !v5 )
    return a1;
  return result;
}


// attributes: thunk
__int64 __fastcall amsg_exit_0(__int64 a1)
{
}int __cdecl matherr(struct _exception *Except)
{
  return 0;
}


__int64 __fastcall FindPESection(__int64 a1, unsigned __int64 a2)
{
  unsigned int v2; // r9d
  __int64 v3; // r8
  __int64 result; // rax
  unsigned __int64 v6; // rdx

  v2 = 0;
  v3 = a1 + *(int *)(a1 + 60);
  result = v3 + *(unsigned __int16 *)(v3 + 20) + 24LL;
  if ( !*(_WORD *)(v3 + 6) )
    return 0;
  while ( 1 )
  {
    v6 = *(unsigned int *)(result + 12);
    if ( a2 >= v6 && a2 < (unsigned int)(v6 + *(_DWORD *)(result + 8)) )
      break;
    ++v2;
    result += 40;
    if ( v2 >= *(unsigned __int16 *)(v3 + 6) )
      return 0;
  }
  return result;
}


__int64 __fastcall IsNonwritableInCurrentImage(__int64 a1)
{
  __int64 result; // rax

  result = ValidateImageBase(0x140000000uLL);
  if ( (_DWORD)result )
  {
    result = FindPESection(0x140000000LL, a1 - 0x140000000LL);
    if ( result )
      return *(int *)(result + 36) >= 0;
  }
  return result;
}


_BOOL8 __fastcall ValidateImageBase(__int64 a1)
{
  __int64 v1; // rax
  _BOOL8 result; // rax

  result = 0;
  if ( *(_WORD *)a1 == 23117 )
  {
    v1 = a1 + *(int *)(a1 + 60);
    if ( *(_DWORD *)v1 == 17744 && *(_WORD *)(v1 + 24) == 523 )
      return 1;
  }
  return result;
}


void __cdecl _security_init_cookie()
{
  uintptr_t v0; // rax
  uintptr_t v1; // rcx
  struct _FILETIME v2; // [rsp+30h] [rbp+10h] BYREF
  struct _FILETIME SystemTimeAsFileTime; // [rsp+38h] [rbp+18h] BYREF
  LARGE_INTEGER PerformanceCount; // [rsp+40h] [rbp+20h] BYREF

  SystemTimeAsFileTime = 0;
  v0 = _security_cookie;
  if ( _security_cookie == 0x2B992DDFA232LL )
  {
    GetSystemTimeAsFileTime(&SystemTimeAsFileTime);
    v2 = SystemTimeAsFileTime;
    v2 = (struct _FILETIME)(GetCurrentProcessId() ^ *(unsigned __int64 *)&v2);
    v2 = (struct _FILETIME)(GetCurrentThreadId() ^ *(unsigned __int64 *)&v2);
    v2 = (struct _FILETIME)(((unsigned __int64)GetTickCount() << 24) ^ *(_QWORD *)&v2);
    v2 = (struct _FILETIME)((unsigned __int64)&v2 ^ *(unsigned __int64 *)&v2 ^ GetTickCount());
    QueryPerformanceCounter(&PerformanceCount);
    v0 = (*(_QWORD *)&v2
        ^ PerformanceCount.QuadPart
        ^ ((unsigned __int64)PerformanceCount.LowPart << 32))
       & 0xFFFFFFFFFFFFLL;
    v1 = v0;
    if ( v0 == 0x2B992DDFA232LL )
    {
      v0 = 0x2B992DDFA233LL;
      v1 = 0x2B992DDFA233LL;
    }
    _security_cookie = v1;
  }
  _security_cookie_complement = ~v0;
}


// attributes: thunk
void __cdecl initterm_0(_PVFV *First, _PVFV *Last)
{
}// attributes: thunk
EXCEPTION_DISPOSITION __cdecl _C_specific_handler_0(
        struct _EXCEPTION_RECORD *ExceptionRecord,
        void *EstablisherFrame,
        struct _CONTEXT *ContextRecord,
        struct _DISPATCHER_CONTEXT *DispatcherContext)
{
}void guard_check_icall_nop()
{
  ;
}


__int64 __fastcall _GSHandlerCheck(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
  _GSHandlerCheckCommon(a2, a4, *(_QWORD *)(a4 + 56));
  return 1;
}


__int64 __fastcall _GSHandlerCheckCommon(__int64 a1, __int64 a2)
{
  __int64 v2; // rcx
  __int64 result; // rax

  v2 = *(unsigned int *)(*(_QWORD *)(a2 + 16) + 8LL);
  result = *(_QWORD *)(a2 + 8);
  if ( (*(_BYTE *)(v2 + result + 3) & 0xF) != 0 )
    return *(_BYTE *)(v2 + result + 3) & 0xF0;
  return result;
}


// attributes: thunk
void *__cdecl memcpy_0(void *a1, const void *Src, size_t Size)
{
}// attributes: thunk
void *__cdecl memset_0(void *a1, int Val, size_t Size)
{
}__int64 __fastcall guard_dispatch_icall_nop()
{
  __int64 (*v0)(void); // rax

  return v0();
}


